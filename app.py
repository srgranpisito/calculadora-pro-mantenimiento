import streamlit as st

# Configuración de página
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

# Título y Diseño
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)
st.write("---")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=500.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: MATERIALES PVC ---
st.header("2. Materiales PVC")
materiales_pvc = {
    "Tubo PVC 20mm (3m)": 2200, "Tubo PVC 25mm (3m)": 2800, "Tubo PVC 32mm (3m)": 3500,
    "Tubo PVC 50mm (3m)": 5200, "Tubo PVC 63mm (3m)": 7500,
    "Válvula PVC 20mm (SO)": 1800, "Válvula PVC 25mm (SO)": 2200,
    "Válvula PVC 32mm (SO)": 2900, "Válvula PVC 50mm (SO)": 4500,
    "Válvula PVC 63mm (SO-HI)": 8900, "Adhesivo PVC (250cc)": 4500
}

totales_pvc = {}
for mat, precio in materiales_pvc.items():
    cant = st.number_input(f"{mat} (${precio} c/u)", min_value=0, step=1, key=mat)
    totales_pvc[mat] = cant * precio

# --- SECCIÓN 3: PERNOS Y FIJACIONES ---
st.header("3. Pernos, Tuercas y Arandelas")
medida = st.selectbox("Selecciona la medida:", ["4mm", "6mm", "8mm", "10mm", "12mm"])
tipo = st.selectbox("Selecciona el tipo:", ["Perno", "Tuerca", "Tornillo", "Arandela"])

# Precio base según tipo y medida
precios_fijaciones = {"Perno": 150, "Tuerca": 80, "Tornillo": 50, "Arandela": 30}
precio_final_fij = precios_fijaciones[tipo] * (int(medida.replace("mm","")) / 4)

cant_fij = st.number_input(f"Cantidad de {tipo} {medida} (${int(precio_final_fij)} c/u)", min_value=0, step=1)
total_fijaciones = cant_fij * precio_final_fij

# --- CÁLCULO FINAL ---
st.divider()
gran_total = sum(totales_pvc.values()) + total_fijaciones + costo_limpieza + costo_hipoclorito + costo_hidro

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")

# --- AVISO LEGAL ---
st.markdown("""
<div style='text-align: center; color: #888888; font-size: 11px;'>
    <hr>
    ⚠️ Nota: Estos precios son aproximados y calculados exclusivamente para el mercado de Chile. 
    Mantenciones Beta no se hace responsable por variaciones en ferreterías locales.
</div>
""", unsafe_allow_html=True)
