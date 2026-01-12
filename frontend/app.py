# Streamlit version sin backend - deploy final

import streamlit as st
import sys
from pathlib import Path

# Permite importar módulos desde la raíz del proyecto
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from backend.pricing_logic import calcular_costo_total

# Configuración de la página
st.set_page_config(
    page_title="PriceFit - IA para Pricing",
    layout="centered"
)

# Título y descripción
st.title("PriceFit – Asistente Inteligente de Pricing para Moda")
st.write("Completa los datos para obtener el precio de venta sugerido.")

# =========================
# Formulario de entrada
# =========================
with st.form("pricing_form"):

    st.subheader("Datos del producto")

    costo_usd = st.number_input(
        "Costo proveedor (USD)",
        min_value=0.0,
        step=0.1
    )

    tipo_cambio = st.number_input(
        "Tipo de cambio (ARS)",
        min_value=0.0,
        step=1.0
    )

    gastos_fijos = st.number_input(
        "Gastos fijos por unidad (ARS)",
        min_value=0.0,
        step=1.0
    )

    impuestos_pct = st.number_input(
        "Impuestos (%)",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )

    categoria = st.selectbox(
        "Categoría del producto",
        ["remera", "pantalón", "campera", "vestido", "accesorios", "otro"]
    )

    objetivo = st.selectbox(
        "Objetivo comercial",
        [
            "maximizar rentabilidad",
            "competir en precio",
            "aumentar rotación",
            "posicionamiento premium"
        ]
    )

    submitted = st.form_submit_button("Calcular precio recomendado")

# =========================
# Resultados
# =========================
if submitted:

    st.subheader("Resultados del cálculo")

    costos = calcular_costo_total(
        costo_usd=costo_usd,
        tipo_cambio=tipo_cambio,
        gastos_fijos=gastos_fijos,
        impuestos_pct=impuestos_pct
    )

    st.write("### Costos detallados")
    st.json(costos)

    # Regla simple de pricing (margen ejemplo)
    margen = 1.4
    precio_sugerido = round(costos["total"] * margen, 2)

    st.success(f"Precio de venta sugerido: ARS {precio_sugerido}")
