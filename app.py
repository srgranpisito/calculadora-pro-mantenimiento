import streamlit as st

# Configuración de página
st.set_page_config(page_title="Mantenciones C&R | Pro", layout="wide")

# Estilo moderno
st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #2E86C1; text-align: center; font-weight: bold; }
    .sub-title { font-size: 1.5rem; color: #555; text-align: center; margin-bottom: 2rem; }
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1; }
    </style>
""", unsafe_allow_html=True)

# Título y Bienvenida
st.markdown("<p class='main-title'>Mantenciones C&R</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Gestión Profesional de Servicios Técnicos</p>", unsafe_allow_html=True)

st.divider()

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🚀 ¿Qué es esta plataforma?")
    st.write("""
    Esta herramienta está diseñada para optimizar tus presupuestos:
    * **Precisión:** Costos detallados de materiales.
    * **Agilidad:** Estimaciones rápidas para terreno.
    * **Formalidad:** Resúmenes listos para entregar.
    """)

with col2:
    st.subheader("💡 Instrucciones")
    st.markdown("""
    <div class='card'>
    1. Dirígete a la sección <strong>Calculadorapro</strong> en el menú lateral.<br>
    2. Ingresa los datos técnicos de tu servicio y materiales.<br>
    3. Visualiza el total y descarga tu presupuesto en formato .txt.
    </div>
    """, unsafe_allow_html=True)

st.write("\n\n")
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>© 2026 Mantenciones C&R</p>", unsafe_allow_html=True)
