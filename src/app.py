import streamlit as st
import pandas as pd
import numpy as np
import mlflow.keras
import os

st.set_page_config(page_title="Predicción de Episodios de Arritmia Cardíaca", layout="centered")

# ---- Título ----
st.title("🫀 Predicción de Episodios de Arritmia Cardíaca")
st.write("Sube un archivo CSV sin encabezados (188 columnas numéricas) para generar una predicción.")

# ---- Cargar modelo (versión MLflow) ----
@st.cache_resource
def cargar_modelo():
    ruta_modelo_mlflow = os.path.join("src", "modelo_mlflow")

    if not os.path.exists(ruta_modelo_mlflow):
        st.error(f"❌ No se encontró el modelo MLflow. Se buscó en: {ruta_modelo_mlflow}")
        return None

    try:
        modelo = mlflow.keras.load_model(ruta_modelo_mlflow)
        st.success("✅ Modelo MLflow cargado correctamente.")
        return modelo
    except Exception as e:
        st.error(f"❌ Error al cargar el modelo MLflow: {e}")
        return None


modelo = cargar_modelo()

# ---- Subir archivo CSV ----
archivo = st.file_uploader("📂 Cargar archivo CSV de prueba", type=["csv"])

if archivo is not None:
    try:
        # Leer CSV sin encabezados
        df = pd.read_csv(archivo, header=None)
        st.write("✅ Archivo cargado correctamente.")
        st.write(f"**Dimensiones:** {df.shape[0]} filas × {df.shape[1]} columnas")

        # Validar columnas esperadas (188)
        if df.shape[1] != 188:
            st.warning(f"⚠️ El archivo tiene {df.shape[1]} columnas, pero el modelo espera 188.")
        else:
            X = df.values.astype(np.float32)

            if modelo is not None:
                # Realizar predicciones
                predicciones = modelo.predict(X)
                st.success("✅ Predicción completada con éxito.")

                # Mostrar tabla de probabilidades
                st.subheader("📊 Resultados de Probabilidades")
                st.dataframe(predicciones)

                # ---- Determinar la clase más probable ----
                clases_predichas = np.argmax(predicciones, axis=1)

                # Mapeo de índices a etiquetas
                etiquetas = {
                    0: "Normal",
                    1: "Fibrilación auricular",
                    2: "Taquicardia",
                    3: "Bradicardia",
                    4: "Otras arritmias"
                }

                nombres_clases = [etiquetas.get(i, "Desconocida") for i in clases_predichas]

                # Mostrar resultados
                st.subheader("🏷️ Diagnóstico Predicho por Muestra")
                resultados_df = pd.DataFrame({
                    "Muestra": range(1, len(clases_predichas) + 1),
                    "Clase (Índice)": clases_predichas,
                    "Diagnóstico": nombres_clases
                })
                st.dataframe(resultados_df)

                # ---- Botón para descargar resultados ----
                csv_resultados = resultados_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="💾 Descargar resultados como CSV",
                    data=csv_resultados,
                    file_name="resultados_prediccion.csv",
                    mime="text/csv"
                )
            else:
                st.error("El modelo no está cargado correctamente. Revisa la ruta o el formato.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("⬆️ Esperando que subas un archivo CSV para realizar la predicción.")
