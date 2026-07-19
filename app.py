import streamlit as st

st.set_page_config(page_title="Acceso - Calculadora Pro", layout="centered")

# Inicializar sesión
if 'logueado' not in st.session_state:
    st.session_state.logueado = False
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

st.title("🔐 Acceso - Calculadora Pro")

# Creamos las dos pestañas
tab1, tab2 = st.tabs(["Ingresar", "Crear Cuenta"])

with tab1:
    user_in = st.text_input("Usuario", key="u_in")
    pass_in = st.text_input("Contraseña", type="password", key="p_in")
    if st.button("Ingresar"):
        if user_in in st.session_state.usuarios and st.session_state.usuarios[user_in] == pass_in:
            st.session_state.logueado = True
            st.switch_page("pages/calculadorapro.py") 
        else:
            st.error("Usuario o contraseña incorrectos")

with tab2:
    new_user = st.text_input("Nuevo Usuario", key="u_new")
    new_pass = st.text_input("Nueva Contraseña", type="password", key="p_new")
    if st.button("Registrar"):
        if new_user in st.session_state.usuarios:
            st.warning("El usuario ya existe")
        elif not new_user or not new_pass:
            st.error("Los campos no pueden estar vacíos")
        else:
            st.session_state.usuarios[new_user] = new_pass
            st.success("Cuenta creada con éxito. Ahora puedes ingresar.")
