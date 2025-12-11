**PRICEFIT – Sistema Inteligente de Pricing para Moda en Argentina**

PriceFit es una aplicación desarrollada para automatizar el cálculo de precios en el sector moda, integrando:

Cálculos financieros tradicionales

Ajustes específicos del mercado argentino

Reglas de margen según categoría

Recomendaciones generadas mediante IA (OpenAI)

El sistema está compuesto por un backend en FastAPI y un frontend interactivo en Streamlit.


*Arquitectura del Proyecto*
pricefit/
│
├── backend/
│   ├── main.py
│   ├── pricing_logic.py
│   └── __init__.py
│
├── frontend/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md

El proyecto se basa en dos módulos:

● Backend (FastAPI)

Expone el endpoint /calcular_precio/

Procesa costos, impuestos y gastos fijos

Interactúa con OpenAI para sugerencias de márgenes y precio final

● Frontend (Streamlit)

Formulario de ingreso de datos

Visualización del costo total

Respuesta dinámica con recomendación de precio final

**Instalacion y Ejecucion**
1. Clonar el repositorio
git clone https://github.com/carolinabenitez23/pricefit.git
cd pricefit

2. Crear entorno virtual
python -m venv venv

3. Activar entorno virtual

Windows PowerShell:

venv\Scripts\Activate.ps1

4. Instalar dependencias
pip install -r requirements.txt

5. Crear archivo .env en la raíz del proyecto
OPENAI_API_KEY="TU_API_KEY_AQUI"

6. Ejecución del Backend (FastAPI)
python -m uvicorn backend.main:app --reload


*La API estará disponible en:*

Documentación interactiva:
http://127.0.0.1:8000/docs

Endpoint principal:
POST /calcular_precio/

7. Ejecución del Frontend (Streamlit)

Desde la raíz del proyecto:

streamlit run frontend/app.py


Se abrirá la interfaz en el navegador.

8. Ejemplo de Uso

Ingresar:

Costo USD: 10

Tipo de cambio: 1200

Gastos fijos: 500

Impuestos: 21 %

Categoría: “Indumentaria Premium”

Objetivo: “Maximizar rentabilidad”

El sistema devuelve:

Costo total ARS

Recomendación de margen según IA

Justificación económica

Precio sugerido final

9. Tecnologías Utilizadas

Python 3.13

FastAPI (backend)

Streamlit (frontend)

OpenAI API

Pydantic

Requests

Git + GitHub

10. Autora

Carolina Benítez
Pre Entrega — IA Prompt Engineering
