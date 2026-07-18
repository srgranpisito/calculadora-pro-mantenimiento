import streamlit as st

st.set_page_config(page_title="Calculadora Pro de Mantenciones Beta")
st.title("🛠️ Calculadora Pro - Mantenciones Beta")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=500.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: MATERIALES (Precios promedio mercado Chile) ---
st.header("2. Materiales de Ferretería")
st.write("Ingresa la cantidad de cada material:")

# Precios basados en promedio de ferreterías chilenas para 20mm
materiales = {
    "Codo 90°": 240,
    "Codo 45°": 120,
    "Tee": 120,
    "Cople": 200,
    "Adaptador Macho/Hembra": 880,
    "Tapón (Tapa gorro)": 420,
    "Válvula de Bola": 490
}

totales_materiales = {}
for material, precio in materiales.items():
    cantidad = st.number_input(f"{material} (aprox. $ {precio} c/u)", min_value=0, step=1)
    totales_materiales[material] = cantidad * precio

# --- CÁLCULO FINAL ---
st.divider()
total_servicios = costo_limpieza + costo_hipoclorito + costo_hidro
total_materiales = sum(totales_materiales.values())
gran_total = total_servicios + total_materiales

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")
st.write(f"Total Servicios: $ {total_servicios:,.0f}")
st.write(f"Total Materiales: $ {total_materiales:,.0f}")
