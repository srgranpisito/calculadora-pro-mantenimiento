import streamlit as st

# --- CONFIGURACIÓN ---
VERSION = "v6.5"
st.set_page_config(page_title="Calculadora Pro - beta", layout="centered")

# --- GESTIÓN DE ESTADO ---
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}
if 'logueado' not in st.session_state:
    st.session_state.logueado = False

# --- LÓGICA DE ACCESO ---
if not st.session_state.logueado:
    st.title("🛠️ Calculadora Pro - beta")
    tab1, tab2 = st.tabs(["Ingresar", "Crear cuenta"])
    
    with tab1:
        user_in = st.text_input("Usuario", key="login_u")
        pass_in = st.text_input("Contraseña", type="password", key="login_p")
        if st.button("Ingresar"):
            if user_in in st.session_state.usuarios and st.session_state.usuarios[user_in] == pass_in:
                st.session_state.logueado = True
                st.rerun()  # <--- Esto fuerza el salto a la calculadora
            else:
                st.error("Credenciales incorrectas.")
                
    with tab2:
        new_u = st.text_input("Nuevo usuario", key="new_u")
        new_p = st.text_input("Nueva contraseña", type="password", key="new_p")
        if st.button("Registrar"):
            if new_u in st.session_state.usuarios:
                st.warning("El usuario ya existe.")
            elif not new_u or not new_p:
                st.error("Completa todos los campos.")
            else:
                st.session_state.usuarios[new_u] = new_p
                st.success("Cuenta creada. Ahora inicia sesión.")
                # No hacemos st.rerun() aquí para que el usuario lea el mensaje
    
    st.stop() # --- IMPORTANTE: Esto impide que la calculadora se cargue antes del login ---

# --- SI LLEGA AQUÍ, EL USUARIO ESTÁ LOGUEADO ---

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1f2937; }
    .stButton>button { width: 100%; background-color: #2E86C1; color: white; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.title("🛠️ Calculadora Pro - beta")
st.markdown("---")

# --- AQUÍ VA TODO TU CÓDIGO DE CÁLCULOS ORIGINAL ---
