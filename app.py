import streamlit as st

# --- CONFIGURACIÓN DE SESIÓN ---
if 'logueado' not in st.session_state:
    st.session_state.logueado = False
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

# --- LÓGICA DE CONTROL (EL "FILTRO") ---
if st.session_state.logueado == False:
    # --- PANTALLA DE LOGIN ---
    st.title("🔐 Acceso - Calculadora Pro")
    
    opcion = st.radio("¿Qué deseas hacer?", ["Ingresar", "Crear cuenta"])
    
    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if opcion == "Ingresar":
        if st.button("Entrar"):
            if usuario in st.session_state.usuarios and st.session_state.usuarios[usuario] == password:
                st.session_state.logueado = True
                st.rerun() # Fuerza la recarga inmediata
            else:
                st.error("Credenciales incorrectas")
    
    elif opcion == "Crear cuenta":
        if st.button("Registrar"):
            if usuario in st.session_state.usuarios:
                st.warning("El usuario ya existe")
            else:
                st.session_state.usuarios[usuario] = password
                st.success("Cuenta creada, ahora selecciona 'Ingresar' para entrar")
    
    st.stop() # DETIENE TODO LO QUE SIGUE HACIA ABAJO

# --- SI LLEGA AQUÍ, EL USUARIO ESTÁ LOGUEADO ---

st.sidebar.button("Cerrar Sesión", on_click=lambda: st.session_state.update({'logueado': False}))

st.title("🛠️ Calculadora Pro - beta")
st.write("Bienvenido a tu sistema de cálculos.")
# AQUÍ PEGAS TODO TU CÓDIGO DE TUBOS, SERVICIOS, ETC.
