import streamlit as st

st.set_page_config(page_title="Calculadora Pro - Mantenciones Beta")
st.title("🛠️ Calculadora Pro - Mantenciones Beta")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=500.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: MATERIALES ---
st.header("2. Materiales de Ferretería")
diametro = st.selectbox("Selecciona el diámetro de la tubería:", ["20mm", "25mm", "32mm"])

# Ajuste de precios según diámetro (ejemplo base para 20mm)
# Si es 25mm o 32mm, multiplicamos el precio base
factor = 1.0 if diametro == "20mm" else (1.4 if diametro == "25mm" else 1.8)

materiales = {
    f"Tubo PVC 3m ({diametro})": int(2500 * factor),
    f"Codo 90° ({diametro})": int(240 * factor),
    f"Codo 45° ({diametro})": int(120 * factor),
    f"Tee ({diametro})": int(120 * factor),
    f"Cople ({diametro})": int(200 * factor),
    f"Adaptador Macho/Hembra ({diametro})": int(880 * factor),
    f"Tapón ({diametro})": int(420 * factor),
    "Válvula de Bola": 490 # Esta suele ser universal
}

totales_materiales = {}
st.write("---")
for material, precio in materiales.items():
    cantidad = st.number_input(f"{material} ($ {precio} c/u)", min_value=0, step=1)
    totales_materiales[material] = cantidad * precio

# --- CÁLCULO FINAL ---
st.divider()
total_servicios = costo_limpieza + costo_hipoclorito + costo_hidro
total_materiales = sum(totales_materiales.values())
gran_total = total_servicios + total_materiales

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")
st.write(f"Total Servicios: $ {total_servicios:,.0f}")
st.write(f"Total Materiales: $ {total_materiales:,.0f}")
