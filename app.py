import streamlit as st

# --- CONFIGURACIÓN Y VERSIÓN ---
VERSION = "v6.3"
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

# --- SECCIÓN 3: CONEXIONES ---
st.header("3. Conexiones y Accesorios")
def selector_accesorio(nombre, precio_base, hilos=["SO", "HI", "SO-HI", "HE-HI"]):
    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
    diam = c1.selectbox(f"Diámetro {nombre}:", [20, 25, 32, 50, 63, 75, 90, 110], key=f"d_{nombre}")
    hilo = c2.selectbox(f"Conex:", hilos, key=f"h_{nombre}")
    cant = c3.number_input(f"Cant:", min_value=0, key=f"c_{nombre}")
    return cant * (precio_base * (1 + (diam/100)))

codo_90 = selector_accesorio("Codo 90°", 500, ["SO", "HI", "SO-HI"])
codo_45 = selector_accesorio("Codo 45°", 450, ["SO", "SO-HI"])
codo_doble = selector_accesorio("Codo Doble", 800, ["SO-HI"])
curva_conduit = selector_accesorio("Curva Conduit", 900, ["HE-HI"])
tee = selector_accesorio("Tee", 600, ["SO-HI"])
copla = selector_accesorio("Copla", 300, ["SO-HI"])
copla_conduit = selector_accesorio("Copla Conduit", 500, ["SO"])
abrazadera = selector_accesorio("Abrazadera", 200, ["SO"])
bajada = selector_accesorio("Bajada", 700)
salida_caja_conduit = selector_accesorio("Salida Caja Conduit", 1000)
terminal_tuerca = selector_accesorio("Terminal c/ Tuerca", 1200)

# --- SECCIÓN 4: FIJACIONES ---
st.header("4. Fijaciones")
def selector_fijacion(nombre, opciones_tipo):
    c1, c2, c3 = st.columns(3)
    diam = c1.selectbox(f"Diám. {nombre}:", ["4mm", "6mm", "8mm", "10mm", "12mm"], key=f"d_{nombre}")
    tipo = c2.selectbox(f"Tipo {nombre}:", opciones_tipo, key=f"t_{nombre}")
    cant = c3.number_input(f"Cant {nombre}:", min_value=0, key=f"c_{nombre}")
    return cant * 150

pernos = selector_fijacion("Perno", ["Zincado", "Inoxidable", "Bronce"])
tuercas = selector_fijacion("Tuerca", ["Hexagonal", "Ciega", "Autofrenante"])
arandelas = selector_fijacion("Arandela", ["Plana", "Presión", "Goma"])

# --- SECCIÓN 5: ADHESIVOS ---
st.header("5. Adhesivos PVC")
c1, c2, c3 = st.columns(3)
cant_trad = c1.number_input("Tradicional:", min_value=0)
cant_hum = c2.number_input("Humedad:", min_value=0)
cant_azul = c3.number_input("Riego (Azul):", min_value=0)
total_adhesivos = (cant_trad * 4500) + (cant_hum * 7500) + (cant_azul * 5500)

# --- CÁLCULO FINAL ---
total_accesorios = codo_90 + codo_45 + codo_doble + curva_conduit + tee + copla + \
                   copla_conduit + abrazadera + bajada + salida_caja_conduit + terminal_tuerca
total_fijaciones = pernos + tuercas + arandelas

gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + precio_tubo + \
             total_accesorios + total_fijaciones + total_adhesivos

st.divider()
st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

# --- EXPORTAR A TXT ---
resumen = f"""Presupuesto Mantenciones C&R
---------------------------
Total Servicios: ${costo_limpieza + costo_hipoclorito + costo_hidro:,.0f}
Total Tubos: ${precio_tubo:,.0f}
Total Accesorios: ${total_accesorios:,.0f}
Total Fijaciones: ${total_fijaciones:,.0f}
Total Adhesivos: ${total_adhesivos:,.0f}

GRAN TOTAL: ${gran_total:,.0f}
---------------------------
Nota: Precios estimados para el mercado de Chile.
"""

st.download_button(
    label="📥 Descargar Presupuesto (.txt)",
    data=resumen,
    file_name="presupuesto_Mantenciones_CyR.txt",
    mime="text/plain"
)

# --- AVISO LEGAL ---
st.divider()
st.markdown("""
<div style='text-align: center; color: #555555; font-size: 12px; font-style: italic;'>
    <strong>Aviso Legal:</strong> Este presupuesto es una estimación referencial basada en valores promedio del mercado nacional chileno. 
    <em>Calculadora Pro</em> no asume responsabilidad alguna ante fluctuaciones, ajustes tarifarios o variaciones de precios en los puntos de venta locales.
</div>
""", unsafe_allow_html=True)
