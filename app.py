import streamlit as st

# --- CONFIGURACIÓN ---
VERSION = "v6.4"
st.set_page_config(page_title="Calculadora Pro", layout="centered")

# Estilos CSS personalizados para un diseño moderno (tipo Wix/Web profesional)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1f2937; font-family: 'Helvetica Neue', sans-serif; }
    h2 { color: #374151; font-size: 20px !important; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #2E86C1; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.title("🛠️ Calculadora Pro - Mantenciones C&R")
st.markdown("---")

# --- SECCIÓN 1: SERVICIOS (Contenedor Estilizado) ---
with st.container():
    st.header("1. Servicios")
    col1, col2, col3 = st.columns(3)
    costo_limpieza = col1.number_input("Limpieza ($)", min_value=0.0, step=1000.0)
    costo_hipoclorito = col2.number_input("Insumos ($)", min_value=0.0, step=500.0)
    costo_hidro = col3.number_input("Hidro ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: TUBOS ---
st.header("2. Tubos")
col_a, col_b, col_c = st.columns(3)
tipo_tubo = col_a.selectbox("Tipo:", ["PVC Agua", "PVC Alcantarillado", "PVC Sanitario", "Conduit"])
diametro_tubo = col_b.selectbox("Diámetro (mm):", [20, 25, 32, 50, 63, 75, 90, 110])
metros = col_c.number_input("Metros:", min_value=0, step=1)
precio_tubo = metros * (diametro_tubo * 120)

# --- SECCIÓN 3: CONEXIONES (Diseño compacto) ---
st.header("3. Conexiones y Accesorios")
def selector_accesorio(nombre, precio_base, hilos=["SO", "HI", "SO-HI", "HE-HI"]):
    c1, c2, c3 = st.columns([2, 1, 1])
    diam = c1.selectbox(f"{nombre} - Diámetro:", [20, 25, 32, 50, 63, 75, 90, 110], key=f"d_{nombre}")
    hilo = c2.selectbox(f"Conex:", hilos, key=f"h_{nombre}")
    cant = c3.number_input(f"Cant:", min_value=0, key=f"c_{nombre}")
    return cant * (precio_base * (1 + (diam/100)))

# Agrupando accesorios para no alargar tanto la pantalla
with st.expander("Ver lista de accesorios y conexiones"):
    codo_90 = selector_accesorio("Codo 90°", 500)
    codo_45 = selector_accesorio("Codo 45°", 450)
    tee = selector_accesorio("Tee", 600)
    copla = selector_accesorio("Copla", 300)
    abrazadera = selector_accesorio("Abrazadera", 200)
    bajada = selector_accesorio("Bajada", 700)
    terminal_tuerca = selector_accesorio("Terminal c/ Tuerca", 1200)

# --- CÁLCULO FINAL ---
total_accesorios = codo_90 + codo_45 + tee + copla + abrazadera + bajada + terminal_tuerca
gran_total = costo_limpieza + costo_hipoclorito + costo_hidro + precio_tubo + total_accesorios

st.markdown("---")
st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

# --- EXPORTAR ---
resumen = f"Presupuesto Mantenciones C&R\nGRAN TOTAL: ${gran_total:,.0f}"
st.download_button("📥 Descargar Presupuesto (.txt)", data=resumen, file_name="presupuesto.txt")
