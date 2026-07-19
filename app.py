import streamlit as st
import json
import os

# --- GESTIÓN DE BASE DE DATOS (Archivo JSON) ---
FILE_NAME = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {"admin": "1234"} # Usuario base si no existe el archivo

def guardar_usuarios(usuarios):
    with open(FILE_NAME, "w") as f:
        json.dump(usuarios, f)

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Acceso - Calculadora Pro", layout="centered")

# --- LÓGICA DE LOGIN ---
if 'logueado' not in st.session_state:
    st.session_state.logueado = False

st.title("🔐 Acceso - Calculadora Pro")
tab1, tab2 = st.tabs(["Ingresar", "Crear Cuenta"])

with tab1:
    user_in = st.text_input("Usuario", key="u_in")
    pass_in = st.text_input("Contraseña", type="password", key="p_in")
    if st.button("Ingresar"):
        usuarios = cargar_usuarios()
        if user_in in usuarios and usuarios[user_in] == pass_in:
            st.session_state.logueado = True
            st.switch_page("pages/calculadorapro.py") 
        else:
            st.error("Usuario o contraseña incorrectos")

with tab2:
    new_user = st.text_input("Nuevo Usuario", key="u_new")
    new_pass = st.text_input("Nueva Contraseña", type="password", key="p_new")
    if st.button("Registrar"):
        usuarios = cargar_usuarios()
        if new_user in usuarios:
            st.warning("El usuario ya existe")
        elif not new_user or not new_pass:
            st.error("Completa los campos")
        else:
            usuarios[new_user] = new_pass
            guardar_usuarios(usuarios)
            st.success("Cuenta creada. Ahora puedes ingresar.")
