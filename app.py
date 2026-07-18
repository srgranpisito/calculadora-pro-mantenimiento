import streamlit as st

# --- CONFIGURACIÓN Y VERSIÓN ---
VERSION = "v5.0"
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
col1, col2, col3 = st.columns(3)
costo_limpieza = col1.number_input("Limpieza ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = col2.number_input("Insumos ($)", min_value=0.0, step=500.0)
costo_hidro = col3.number_input("Hidro ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: TUBOS ---
st.header("2. Tubos")
tipo_tubo = st.selectbox("Tipo de Tubo:", ["PVC Agua", "PVC Alcantarillado", "PVC Sanitario", "Conduit"])
diametro_tubo = st.selectbox("Diámetro (mm):", [20, 25, 32, 50, 63, 75, 90, 110], key="tubo_diam")
metros = st.number_input("Metros de Tubo:", min_value=0, step=1)
precio_tubo = metros * (diametro_tubo * 120)

# --- SECCIÓN 3: CONEXIONES Y ACCESORIOS (Con selector individual) ---
st.header("3. Conexiones y Accesorios")

def selector_accesorio(nombre, precio_base):
    col_a, col_b = st.columns([2, 1])
    diam = col_a.selectbox(f"Diámetro para {nombre}:", [20, 25, 32, 50, 63, 75, 90, 110], key=f"d_{nombre}")
    cant = col_b.number_input(f"Cant:", min_value=0, key=f"c_{nombre}")
    # El precio aumenta un poco según el diámetro
    return cant * (precio_base * (1 + (diam/100)))

# Lista de accesorios
codo_90 = selector_accesorio("Codo 90°", 500)
codo_45 = selector_accesorio("Codo 45°", 450)
codo_doble = selector_accesorio("Codo Doble", 800)
curva_conduit = selector_accesorio("Curva Conduit", 900)
tee = selector_accesorio("Tee", 600)
copla = selector_accesorio("Copla", 300)
copla_conduit = selector_accesorio("Copla Conduit", 500)
abrazadera = selector_accesorio("Abrazadera", 200)
bajada = selector_accesorio("Bajada", 700)
salida_caja_conduit = selector_accesorio("Salida Caja Conduit", 1000)
terminal_tuerca = selector_accesorio("Terminal c/ Tuerca", 1200)

# --- SECCIÓN 4: FIJACIONES ---
st.header("4. Pernos, Tuercas y Arandelas")
cant_fij = st.number_input("Cantidad de fijaciones:", min_value=0, step=1)
total_fijaciones = cant_fij * 150

# --- CÁLCULO FINAL ---
total_accesorios = codo_90 + codo_45 + codo_doble + curva_conduit + tee + copla + \
                   copla_conduit + abrazadera + bajada + salida_caja_conduit + terminal_tuerca

gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + precio_tubo + total_accesorios + total_fijaciones

st.divider()
st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

st.markdown("""
<div style='text-align: center; color: #888888; font-size: 11px;'>
    <hr>
    ⚠️ Nota: Precios estimados y calculados exclusivamente para el mercado de Chile.
</div>
""", unsafe_allow_html=True)
