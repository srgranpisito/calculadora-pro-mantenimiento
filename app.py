import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Calculadora Pro - beta", layout="centered")

# --- CONTROL DE ESTADO ---
if 'logueado' not in st.session_state:
    st.session_state.logueado = False
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

# --- PANTALLA DE LOGIN ---
def mostrar_login():
    st.title("🔐 Acceso - Calculadora Pro")
    menu = st.radio("Acción:", ["Ingresar", "Crear cuenta"])
    
    user = st.text_input("Usuario")
    pw = st.text_input("Contraseña", type="password")
    
    if st.button("Ejecutar"):
        if menu == "Ingresar":
            if user in st.session_state.usuarios and st.session_state.usuarios[user] == pw:
                st.session_state.logueado = True
                st.rerun() # Fuerza recarga inmediata
            else:
                st.error("Datos incorrectos")
        else:
            if user in st.session_state.usuarios:
                st.warning("Usuario ya existe")
            elif user and pw:
                st.session_state.usuarios[user] = pw
                st.success("Cuenta creada, ahora ingresa")
            else:
                st.error("Campos vacíos")

# --- PANTALLA PRINCIPAL ---
def mostrar_calculadora():
    st.sidebar.button("Cerrar Sesión", on_click=lambda: st.session_state.update({'logueado': False, 'rerun': st.rerun()}))
    st.title("🛠️ Calculadora Pro - beta")
    st.write("---")
    # AQUÍ PEGARÁS TU CÓDIGO DE CÁLCULOS
    st.success("Bienvenido a la calculadora")

# --- EJECUCIÓN ---
if not st.session_state.logueado:
    mostrar_login()
else:
    mostrar_calculadora()
