import os
import sys
import numpy as np
import pandas as pd
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prediccion import generar_predicciones


def test_generar_predicciones():
    """
    Prueba la función generar_predicciones utilizando un modelo simulado (mock).

    Crea un DataFrame de entrada con dos muestras y simula un modelo que retorna predicciones predefinidas.
    Verifica que:
    - La salida de predicciones coincida exactamente con lo que retorna el modelo simulado.
    - El DataFrame de resultados contenga los índices de clase correctos y los nombres de diagnóstico esperados,
      según el diccionario ETIQUETAS.

    Esta prueba valida tanto la lógica de clasificación como la construcción del DataFrame de salida.
    """

    df_mock = pd.DataFrame([[0.1, 0.2], [0.3, 0.4]])

    # Simula el modelo con MagicMock
    modelo_mock = MagicMock()
    modelo_mock.predict.return_value = np.array([
        [0.1, 0.7, 0.2],  # clase 1
        [0.8, 0.1, 0.1]   # clase 0
    ])

    # Ejecuta la función
    predicciones, resultados_df = generar_predicciones(modelo_mock, df_mock)

    # Verifica las predicciones
    np.testing.assert_array_equal(predicciones, modelo_mock.predict.return_value)

    # Verifica el DataFrame de resultados
    expected_df = pd.DataFrame({
        "Muestra": [1, 2],
        "Clase (Índice)": [1, 0],
        "Diagnóstico": ["Fibrilación auricular", "Normal"]
    })
    pd.testing.assert_frame_equal(resultados_df, expected_df)