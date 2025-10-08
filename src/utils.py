import streamlit as st

# Diccionario de etiquetas (clases del modelo)
ETIQUETAS = {
    0: "Normal",
    1: "Fibrilación auricular",
    2: "Taquicardia",
    3: "Bradicardia",
    4: "Otras arritmias"
}

def validar_columnas(df, columnas_esperadas=188):
    """
    Valida que el DataFrame tenga el número de columnas esperado.
    """
    if df.shape[1] != columnas_esperadas:
        st.warning(f"⚠️ El archivo tiene {df.shape[1]} columnas, pero el modelo espera {columnas_esperadas}.")
        return False
    return True
