import streamlit as st

st.set_page_config(page_title="Calculadora Pro de Mantenimiento")
st.title("🛠️ Calculadora Pro de Mantenimiento")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=1000.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: MATERIALES ---
st.header("2. Materiales de Ferretería")

if 'num_items' not in st.session_state:
    st.session_state.num_items = 1

if st.button("Agregar otro material"):
    st.session_state.num_items += 1

total_materiales = 0
for i in range(st.session_state.num_items):
    col1, col2, col3 = st.columns(3)
    with col1:
        nombre = st.text_input(f"Ítem {i+1}", key=f"nombre_{i}")
    with col2:
        cant = st.number_input("Cant.", min_value=0, key=f"cant_{i}")
    with col3:
        precio = st.number_input("Precio Unit ($)", min_value=0.0, step=100.0, key=f"precio_{i}")
    
    total_materiales += (cant * precio)

# --- RESULTADO FINAL ---
total_general = costo_limpieza + costo_hipoclorito + costo_hidro + total_materiales

st.divider()
st.subheader(f"Total Presupuesto: ${total_general:,.0f}")
