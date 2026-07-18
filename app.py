import streamlit as st

# --- CONFIGURACIÓN Y VERSIÓN ---
VERSION = "v2.1"
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)
st.write("---")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=500.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: TUBOS PVC (NUEVO) ---
st.header("2. Tubos PVC")
tipo_tubo = st.selectbox("Selecciona el tipo de tubo:", 
                         ["Agua (Cementar)", "Alcantarillado (Gris)", "Sanitario (Gris)", "Presión (Clase 10)"])
diametro = st.select_slider("Diámetro (mm):", options=[20, 25, 32, 50, 63, 75, 90, 110])
metros = st.number_input("Cantidad de metros:", min_value=0, step=1)

# Lógica de precios (Ejemplo base multiplicado por tipo y diámetro)
multiplicador = {"Agua (Cementar)": 1.0, "Alcantarillado (Gris)": 1.2, "Sanitario (Gris)": 1.1, "Presión (Clase 10)": 1.5}
precio_base_mt = (diametro * 100) * multiplicador[tipo_tubo]
total_tubos = metros * precio_base_mt

st.write(f"**Precio estimado por metro:** $ {precio_base_mt:,.0f}")

# --- SECCIÓN 3: PERNOS Y FIJACIONES ---
st.header("3. Pernos, Tuercas y Arandelas")
medida = st.selectbox("Medida de fijación:", ["4mm", "6mm", "8mm", "10mm", "12mm"])
tipo = st.selectbox("Tipo:", ["Perno", "Tuerca", "Tornillo", "Arandela"])

precios_fij = {"Perno": 150, "Tuerca": 80, "Tornillo": 50, "Arandela": 30}
precio_uni = precios_fij[tipo] * (int(medida.replace("mm","")) / 4)
cant_fij = st.number_input(f"Cantidad de {tipo} {medida}", min_value=0, step=1)
total_fijaciones = cant_fij * precio_uni

# --- CÁLCULO FINAL ---
st.divider()
gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + total_tubos + total_fijaciones

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

# --- AVISO LEGAL ---
st.markdown("""
<div style='text-align: center; color: #888888; font-size: 11px;'>
    <hr>
    ⚠️ Nota: Precios estimados y calculados exclusivamente para el mercado de Chile. 
    Mantenciones Beta no se hace responsable por variaciones en ferreterías locales.
</div>
""", unsafe_allow_html=True)
