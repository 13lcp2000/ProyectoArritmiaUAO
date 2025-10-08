import streamlit as st
import mlflow.keras
import os

@st.cache_resource
def cargar_modelo_mlflow():
    """
    Carga el modelo entrenado desde MLflow.
    """
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
