import streamlit as st

# Configuración de página
st.set_page_config(page_title="Calculadora Pro Mantenciones Beta", layout="centered")

# Diseño personalizado con HTML
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🛠️ Calculadora Pro - Mantenciones Beta</h1>", unsafe_allow_html=True)
st.write("---")

# --- SECCIÓN 1: SERVICIOS ---
st.header("1. Servicios")
costo_limpieza = st.number_input("Costo Limpieza y Cepillado ($)", min_value=0.0, step=1000.0)
costo_hipoclorito = st.number_input("Costo Insumos (Hipoclorito) ($)", min_value=0.0, step=500.0)
costo_hidro = st.number_input("Costo Hidrolavado ($)", min_value=0.0, step=1000.0)

# --- SECCIÓN 2: MATERIALES ---
st.header("2. Materiales de Ferretería")

# Lista de materiales
materiales = {
    "Tubo PVC 20mm (3m)": 2200,
    "Tubo PVC 25mm (3m)": 2800,
    "Tubo PVC 32mm (3m)": 3500,
    "Tubo PVC 50mm (3m)": 5200,
    "Tubo PVC 63mm (3m)": 7500,
    "Válvula PVC 20mm (SO)": 1800,
    "Válvula PVC 25mm (SO)": 2200,
    "Válvula PVC 32mm (SO)": 2900,
    "Válvula PVC 50mm (SO)": 4500,
    "Válvula PVC 63mm (SO-HI)": 8900,
    "Adhesivo PVC (Tarro 250cc)": 4500
}

totales_materiales = {}

# Mostrar materiales en dos columnas
lista_items = list(materiales.items())
for i in range(0, len(lista_items), 2):
    c1, c2 = st.columns(2)
    
    # Columna izquierda
    item1 = lista_items[i]
    cant1 = c1.number_input(f"{item1[0]} (${item1[1]})", min_value=0, step=1, key=item1[0])
    totales_materiales[item1[0]] = cant1 * item1[1]
    
    # Columna derecha (si existe)
    if i + 1 < len(lista_items):
        item2 = lista_items[i+1]
        cant2 = c2.number_input(f"{item2[0]} (${item2[1]})", min_value=0, step=1, key=item2[0])
        totales_materiales[item2[0]] = cant2 * item2[1]

# --- CÁLCULO FINAL ---
st.divider()
total_servicios = costo_limpieza + costo_hipoclorito + costo_hidro
total_materiales = sum(totales_materiales.values())
gran_total = total_servicios + total_materiales

st.subheader(f"💰 Total Presupuesto: $ {gran_total:,.0f}")
st.write(f"**Total Servicios:** $ {total_servicios:,.0f}")
st.write(f"**Total Materiales:** $ {total_materiales:,.0f}")

# --- AVISO LEGAL ---
st.write("")
st.markdown("""
<div style='text-align: center; color: #888888; font-size: 12px;'>
    <hr>
    ⚠️ Nota: Todos los cálculos presentados en esta herramienta son estimados y están sujetos a variaciones según los precios de mercado actuales. 
    Mantenciones Beta no se hace responsable por diferencias menores en precios de insumos.
</div>
""", unsafe_allow_html=True)
