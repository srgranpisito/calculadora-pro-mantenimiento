# --- EXPORTAR A TXT ---
st.divider()
st.subheader("📥 Exportar Presupuesto")

resumen = f"""Presupuesto Mantenciones Beta
---------------------------
Total Servicios: ${costo_limpieza + costo_hipoclorito + costo_hidro:,.0f}
Total Tubos: ${precio_tubo:,.0f}
Total Accesorios: ${total_accesorios:,.0f}
Total Fijaciones: ${total_fijaciones:,.0f}
Total Adhesivos: ${total_adhesivos:,.0f}

GRAN TOTAL: ${gran_total:,.0f}
---------------------------
Nota: Precios estimados para Chile.
"""

st.download_button(
    label="Descargar Presupuesto (.txt)",
    data=resumen,
    file_name="presupuesto_mantenciones.txt",
    mime="text/plain"
)
