import streamlit as st

# --- CONFIGURACIÓN ---
VERSION = "v6.5"
st.set_page_config(page_title="Calculadora Pro - beta", layout="centered")

# --- LOBBY (ACCESO) ---
if 'logueado' not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    st.title("🔐 Acceso")
    st.subheader("Calculadora Pro - beta")
    
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Ingresar"):
        # Ajusta tus credenciales aquí
        if user == "admin" and password == "admin":
            st.session_state.logueado = True
            st.rerun()
        else:
            st.error("Credenciales incorrectas")
    st.stop()

# --- APP PRINCIPAL ---
# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1f2937; }
    .stButton>button { width: 100%; background-color: #2E86C1; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Botón para cerrar sesión en la barra lateral
if st.sidebar.button("Cerrar Sesión"):
    st.session_state.logueado = False
    st.rerun()

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.title("🛠️ Calculadora Pro - beta")
st.markdown("---")

# --- RESTO DEL CÓDIGO (Servicios, Tubos, etc.) ---
# ... (Aquí va todo tu código original) ...
