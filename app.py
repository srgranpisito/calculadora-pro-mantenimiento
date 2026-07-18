import streamlit as st

# --- CONFIGURACIÓN Y VERSIÓN ---
VERSION = "v4.0"
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
col1, col2, col3 = st.columns(3)
costo_limpieza = col1.number_input("Limpieza ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = col2.number_input("Insumos ($)", min_value=0.0, step=500.0)
costo_hidro = col3.number_input("Hidro ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: TUBOS (PVC Y CONDUIT) ---
st.header("2. Tubos")
tipo_tubo = st.selectbox("Tipo de Tubo:", ["PVC Agua", "PVC Alcantarillado", "PVC Sanitario", "Conduit"])
diametro_tubo = st.selectbox("Diámetro (mm):", [20, 25, 32, 50, 63, 75, 90, 110])
metros = st.number_input("Metros de Tubo:", min_value=0, step=1)
precio_tubo = metros * (diametro_tubo * 120) # Lógica de precio base

# --- SECCIÓN 3: CONEXIONES Y ACCESORIOS ---
st.header("3. Conexiones y Accesorios")
# Separamos cada uno para que tengas su barrita individual
codo_90 = st.number_input("Codo 90°:", min_value=0)
codo_45 = st.number_input("Codo 45°:", min_value=0)
codo_doble = st.number_input("Codo Doble:", min_value=0)
curva_conduit = st.number_input("Curva Conduit (Indicar grados):", min_value=0)
tee = st.number_input("Tee:", min_value=0)
copla = st.number_input("Copla:", min_value=0)
copla_conduit = st.number_input("Copla Conduit:", min_value=0)
abrazadera = st.number_input("Abrazaderas:", min_value=0)
bajada = st.number_input("Bajadas:", min_value=0)
salida_caja_conduit = st.number_input("Salida Caja Conduit:", min_value=0)
terminal_tuerca = st.number_input("Terminal con Tuerca:", min_value=0)

# --- SECCIÓN 4: FIJACIONES ---
st.header("4. Pernos, Tuercas y Arandelas")
cant_fij = st.number_input("Cantidad de fijaciones:", min_value=0)

# --- CÁLCULO FINAL ---
total_materiales = precio_tubo + (codo_90*500) + (codo_45*450) + (codo_doble*800) + \
                   (curva_conduit*900) + (tee*600) + (copla*300) + (copla_conduit*500) + \
                   (abrazadera*200) + (bajada*700) + (salida_caja_conduit*1000) + \
                   (terminal_tuerca*1200) + (cant_fij*150)

gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + total_materiales

st.divider()
st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

st.markdown("""
<div style='text-align: center; color: #888888; font-size: 11px;'>
    <hr>
    ⚠️ Nota: Precios estimados y calculados exclusivamente para el mercado de Chile.
</div>
""", unsafe_allow_html=True)
