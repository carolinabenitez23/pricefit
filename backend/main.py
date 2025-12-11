from fastapi import FastAPI
from pydantic import BaseModel
from backend.pricing_logic import calcular_costo_total
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
import os
import json

# Ruta ABSOLUTA al archivo .env
ENV_PATH = Path(r"C:\Users\ACER\Documents\CODER\ia2\pricefit\.env")
load_dotenv(dotenv_path=ENV_PATH)

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Modelo de datos
class PricingRequest(BaseModel):
    costo_usd: float
    tipo_cambio: float
    gastos_fijos: float
    impuestos_pct: float
    categoria: str
    objetivo: str


@app.post("/calcular_precio/")
def calcular_precio(data: PricingRequest):

    # 1. Calcular costos internos
    costo_local = calcular_costo_total(
        data.costo_usd,
        data.tipo_cambio,
        data.gastos_fijos,
        data.impuestos_pct
    )

    # 2. Preparar prompt
    prompt = f"""
Eres un asistente experto en pricing para moda en Argentina.

Datos:
- Costo proveedor USD: {data.costo_usd}
- Tipo de cambio: {data.tipo_cambio}
- Gastos fijos por unidad: {data.gastos_fijos}
- Impuestos (%): {data.impuestos_pct}
- Costo total (ARS): {costo_local["total"]}
- Categoría: {data.categoria}
- Objetivo comercial: {data.objetivo}

Devuelve SOLO un JSON con:
- margen_sugerido
- razonamiento
- precio_recomendado_ars
"""

    # 3. Intentar llamar a OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        respuesta_ai = response.choices[0].message["content"]

        # Intentamos parsear el JSON devuelto
        try:
            parsed_ai = json.loads(respuesta_ai)
        except:
            parsed_ai = {"respuesta_texto": respuesta_ai}

    except Exception as e:
        # 4. Si OpenAI falla → SIMULACIÓN
        parsed_ai = {
            "margen_sugerido": "50%",
            "razonamiento": f"Simulación porque OpenAI falló: {str(e)}",
            "precio_recomendado_ars": costo_local["total"] * 1.5
        }

    # 5. Respuesta final
    return {
        "costo_detalle": costo_local,
        "ia_respuesta": parsed_ai
    }
