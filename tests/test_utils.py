import os
import sys
import pandas as pd
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import validar_columnas

def test_validar_columnas_correctas():
    """
    Prueba que la función validar_columnas retorne True cuando el DataFrame tiene el número correcto de columnas.

    Crea un DataFrame simulado con 188 columnas (valor esperado por defecto) y verifica que la validación sea exitosa.
    """
    df = pd.DataFrame([[1]*188, [2]*188])  # DataFrame con 188 columnas
    assert validar_columnas(df) is True

@patch("src.utils.st.warning")
def test_validar_columnas_incorrectas(mock_warning):
    """
    Prueba que la función validar_columnas retorne False y emita una advertencia cuando el número de columnas es incorrecto.

    Simula un DataFrame con 150 columnas y verifica que:
    - La función retorne False.
    - Se llame a st.warning con el mensaje esperado.
    """
    df = pd.DataFrame([[1]*150, [2]*150])  # DataFrame con columnas incorrectas
    resultado = validar_columnas(df)
    assert resultado is False
    mock_warning.assert_called_once_with("⚠️ El archivo tiene 150 columnas, pero el modelo espera 188.")
