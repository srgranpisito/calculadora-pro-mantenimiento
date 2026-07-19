import streamlit as st

# --- CONFIGURACIÓN ---
VERSION = "v6.5"
st.set_page_config(page_title="Calculadora Pro - beta", layout="centered")

# --- BASE DE DATOS TEMPORAL EN SESIÓN ---
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"} # Usuario por defecto

if 'logueado' not in st.session_state:
    st.session_state.logueado = False

# --- LOBBY (ACCESO / CREAR CUENTA) ---
if not st.session_state.logueado:
    st.title("🔐 Calculadora Pro - beta")
    
    tab1, tab2 = st.tabs(["Ingresar", "Crear Cuenta"])
    
    with tab1:
        user_login = st.text_input("Usuario", key="u_log")
        pass_login = st.text_input("Contraseña", type="password", key="p_log")
        if st.button("Ingresar"):
            if user_login in st.session_state.usuarios and st.session_state.usuarios[user_login] == pass_login:
                st.session_state.logueado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")
                
    with tab2:
        new_user = st.text_input("Nuevo Usuario", key="u_new")
        new_pass = st.text_input("Nueva Contraseña", type="password", key="p_new")
        if st.button("Registrar"):
            if new_user in st.session_state.usuarios:
                st.warning("El usuario ya existe")
            elif new_user == "" or new_pass == "":
                st.error("Los campos no pueden estar vacíos")
            else:
                st.session_state.usuarios[new_user] = new_pass
                st.success("Cuenta creada con éxito. Ve a la pestaña 'Ingresar'")
    st.stop()

# --- APP PRINCIPAL (Solo visible si logueado) ---
st.sidebar.write(f"Sesión activa")
if st.sidebar.button("Cerrar Sesión"):
    st.session_state.logueado = False
    st.rerun()

st.markdown(f"<p style='text-align: right; color: #888; font-size: 10px;'>Versión: {VERSION}</p>", unsafe_allow_html=True)
st.title("🛠️ Calculadora Pro - beta")
st.markdown("---")

# ... (Aquí iría todo tu código original de servicios, tubos, etc.) ...
