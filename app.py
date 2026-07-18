import streamlit as st

# Configuración de página
st.set_page_config(page_title="Gestión de Servicios Pro", layout="wide")

# Estilo moderno
st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #2E86C1; text-align: center; font-weight: bold; }
    .sub-title { font-size: 1.5rem; color: #555; text-align: center; margin-bottom: 2rem; }
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1; }
    </style>
""", unsafe_allow_html=True)

# Título y Bienvenida (sin el nombre de la empresa)
st.markdown("<p class='main-title'>Portal de Gestión Técnica</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Herramienta Profesional de Cotización</p>", unsafe_allow_html=True)

st.divider()

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🚀 Acerca de esta herramienta")
    st.write("""
    Plataforma técnica optimizada para el cálculo preciso de presupuestos:
    * **Precisión:** Estimación técnica de materiales e insumos.
    * **Agilidad:** Flujo de trabajo rápido para terreno.
    * **Formalidad:** Generación de resúmenes profesionales listos para entrega.
    """)

with col2:
    st.subheader("💡 Instrucciones")
    st.markdown("""
    <div class='card'>
    1. Dirígete a la sección <strong>Calculadorapro</strong> en el menú lateral.<br>
    2. Ingresa los parámetros técnicos de tu servicio.<br>
    3. Calcula el total y descarga tu presupuesto en formato .txt.
    </div>
    """, unsafe_allow_html=True)

st.write("\n\n")
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>© 2026 Sistema de Gestión Técnica</p>", unsafe_allow_html=True)
