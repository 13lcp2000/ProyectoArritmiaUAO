import numpy as np
import pandas as pd
from .utils import ETIQUETAS

def generar_predicciones(modelo, df):
    """
    Realiza las predicciones del modelo sobre un DataFrame cargado.
    """
    X = df.values.astype(np.float32)
    predicciones = modelo.predict(X)
    clases_predichas = np.argmax(predicciones, axis=1)
    nombres_clases = [ETIQUETAS.get(i, "Desconocida") for i in clases_predichas]

    resultados_df = pd.DataFrame({
        "Muestra": range(1, len(clases_predichas) + 1),
        "Clase (Índice)": clases_predichas,
        "Diagnóstico": nombres_clases
    })

    return predicciones, resultados_df
