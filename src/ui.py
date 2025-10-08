import streamlit as st

def mostrar_resultados(predicciones, resultados_df):
    """
    Muestra los resultados de las predicciones y permite descargarlos.
    """
    st.success("✅ Predicción completada con éxito.")
    st.subheader("📊 Resultados de Probabilidades")
    st.dataframe(predicciones)

    st.subheader("🏷️ Diagnóstico Predicho por Muestra")
    st.dataframe(resultados_df)

    csv_resultados = resultados_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="💾 Descargar resultados como CSV",
        data=csv_resultados,
        file_name="resultados_prediccion.csv",
        mime="text/csv"
    )
