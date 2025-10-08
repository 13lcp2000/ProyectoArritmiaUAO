import streamlit as st
import pandas as pd
from cargar_modelo import cargar_modelo_mlflow
from prediccion import generar_predicciones
from utils import validar_columnas
from ui import mostrar_resultados

st.set_page_config(page_title="Predicción de Episodios de Arritmia Cardíaca", layout="centered")

# ---- Título ----
st.title("🫀 Predicción de Episodios de Arritmia Cardíaca")
st.write("Sube un archivo CSV sin encabezados (188 columnas numéricas) para generar una predicción.")

# ---- Cargar modelo ----
modelo = cargar_modelo_mlflow()

# ---- Subir archivo CSV ----
archivo = st.file_uploader("📂 Cargar archivo CSV de prueba", type=["csv"])

if archivo is not None:
    try:
        df = pd.read_csv(archivo, header=None)
        st.write("✅ Archivo cargado correctamente.")
        st.write(f"**Dimensiones:** {df.shape[0]} filas × {df.shape[1]} columnas")

        if validar_columnas(df):
            if modelo is not None:
                predicciones, resultados_df = generar_predicciones(modelo, df)
                mostrar_resultados(predicciones, resultados_df)
            else:
                st.error("El modelo no está cargado correctamente. Revisa la ruta o el formato.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("⬆️ Esperando que subas un archivo CSV para realizar la predicción.")