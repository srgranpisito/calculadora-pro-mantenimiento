import streamlit as st

# --- CONFIGURACIÓN Y VERSIÓN ---
VERSION = "v3.0"
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
col_s1, col_s2, col_s3 = st.columns(3)
costo_limpieza = col_s1.number_input("Limpieza ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = col_s2.number_input("Insumos ($)", min_value=0.0, step=500.0)
costo_hidro = col_s3.number_input("Hidro ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: TUBOS Y CONEXIONES (NUEVA ESTRUCTURA) ---
st.header("2. Materiales por Diámetro")
diametro = st.select_slider("Selecciona el Diámetro (mm):", options=[20, 25, 32, 50, 63, 75, 90, 110])

# Precios base estimados por diámetro (puedes ajustar estos valores)
base = diametro * 50 

st.subheader(f"Tubos y Accesorios ({diametro}mm)")
metros = st.number_input("Metros de Tubo:", min_value=0, step=1)
codo_90 = st.number_input("Codos 90°:", min_value=0, step=1)
codo_45 = st.number_input("Codos 45°:", min_value=0, step=1)
tee = st.number_input("Tees:", min_value=0, step=1)
copla = st.number_input("Coplas/Uniones:", min_value=0, step=1)
adaptador = st.number_input("Adaptadores (M/H):", min_value=0, step=1)
valvula = st.number_input("Válvulas de Paso:", min_value=0, step=1)

# Cálculo materiales
total_materiales = (metros * (base * 2)) + (codo_90 * (base*0.5)) + (codo_45 * (base*0.4)) + \
                   (tee * (base*0.6)) + (copla * (base*0.3)) + (adaptador * (base*0.8)) + (valvula * (base*3))

# --- SECCIÓN 3: PERNOS Y FIJACIONES ---
st.header("3. Fijaciones")
cant_fij = st.number_input("Cantidad de Pernos/Tuercas/Arandelas:", min_value=0, step=1)
total_fijaciones = cant_fij * 200 # Precio promedio fijación

# --- CÁLCULO FINAL ---
st.divider()
gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + total_materiales + total_fijaciones

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

# --- AVISO LEGAL ---
st.markdown("""
<div style='text-align: center; color: #888888; font-size: 11px;'>
    <hr>
    ⚠️ Nota: Precios estimados y calculados exclusivamente para el mercado de Chile. 
    Mantenciones Beta no se hace responsable por variaciones en ferreterías locales.
</div>
""", unsafe_allow_html=True)
