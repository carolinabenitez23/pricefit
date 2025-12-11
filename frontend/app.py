import streamlit as st
import requests
import pandas as pd

st.title("PriceFit – Asistente Inteligente de Precios")

st.header("Ingresar datos del producto")

costo_usd = st.number_input("Costo proveedor (USD)", min_value=0.0)
tipo_cambio = st.number_input("Tipo de cambio", min_value=0.0)
gastos_fijos = st.number_input("Gastos fijos por unidad (ARS)", min_value=0.0)
impuestos_pct = st.number_input("Impuestos (%)", min_value=0.0)
categoria = st.text_input("Categoría del producto", "remera básica")
objetivo = st.selectbox("Objetivo comercial", ["venta rápida", "mantener margen", "premium"])

if st.button("Calcular precio con IA"):

    payload = {
        "costo_usd": costo_usd,
        "tipo_cambio": tipo_cambio,
        "gastos_fijos": gastos_fijos,
        "impuestos_pct": impuestos_pct,
        "categoria": categoria,
        "objetivo": objetivo
    }

    response = requests.post("http://127.0.0.1:8000/calcular_precio/", json=payload)

    if response.status_code == 200:
        data = response.json()
        
        st.subheader("Costo total (ARS)")
        st.json(data["costo_detalle"])

        st.subheader("Respuesta de la IA")
        st.write(data["ia_respuesta"])

    else:
        st.error("Error llamando a la API")
