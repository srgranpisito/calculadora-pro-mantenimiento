import streamlit as st

st.set_page_config(page_title="Inicio de Sesión", layout="centered")

if 'logueado' not in st.session_state:
    st.session_state.logueado = False
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

st.title("🔐 Acceso - Calculadora Pro")

# Formulario de Login
user = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Ingresar"):
    if user in st.session_state.usuarios and st.session_state.usuarios[user] == password:
        st.session_state.logueado = True
        # AQUÍ ESTÁ LA MAGIA: Redirige automáticamente a la página en la carpeta 'pages'
        st.switch_page("pages/calculadorapro.py") 
    else:
        st.error("Credenciales incorrectas")
