import os
import pytest
import numpy as np
import pandas as pd
from tensorflow import keras

# --- UTILS Y CONSTANTES ---
# La ruta corregida que ya validamos que funciona en local y Docker
MODEL_PATH = os.path.join("src", "modelo", "PrediccionArritmia.keras")

# Dimensiones esperadas del modelo: EL MODELO ESPERA 187 COLUMNAS SEGÚN LA PRUEBA
EXPECTED_TIMESTEPS = 187 
EXPECTED_CHANNELS = 1 # El modelo CNN usa 1 canal (ej: (None, 187, 1))
EXPECTED_OUTPUT_SHAPE = 5
SAMPLE_SIZE = 10 # Número de muestras para pruebas

# --- PRUEBAS ---

def test_01_model_file_exists():
    """
    Verifica que el archivo del modelo Keras exista en la ruta esperada.
    """
    assert os.path.exists(MODEL_PATH), f"El archivo del modelo NO fue encontrado en: {MODEL_PATH}"

@pytest.fixture(scope="session")
def loaded_model():
    """
    Fixture para cargar el modelo una sola vez para todas las pruebas.
    """
    try:
        # Se asegura de que la prueba falle si no se puede cargar el modelo
        modelo = keras.models.load_model(MODEL_PATH)
        return modelo
    except Exception as e:
        pytest.fail(f"Fallo al cargar el modelo con keras.models.load_model: {e}")

def test_02_model_is_loaded(loaded_model):
    """
    Verifica que el objeto devuelto sea una instancia válida de un modelo de Keras.
    """
    assert isinstance(loaded_model, keras.Model), "El objeto cargado no es un modelo de Keras."
    
def test_03_model_input_shape(loaded_model):
    """
    Verifica que la forma de entrada del modelo sea la esperada (187 pasos, 1 canal).
    """
    # Para modelos CNN de series de tiempo, el input_shape es típicamente (None, Timesteps, Channels)
    input_shape = loaded_model.input_shape
    
    # Verificamos los dos últimos elementos: Timesteps (187) y Channels (1)
    assert input_shape[-2] == EXPECTED_TIMESTEPS, \
        f"El número de pasos de tiempo (columnas) esperado es {EXPECTED_TIMESTEPS}, pero se encontró {input_shape[-2]}."
        
    assert input_shape[-1] == EXPECTED_CHANNELS, \
        f"El número de canales esperado es {EXPECTED_CHANNELS}, pero se encontró {input_shape[-1]}. El modelo es probablemente una CNN."

def test_04_model_output_shape(loaded_model):
    """
    Verifica que la forma de salida del modelo sea la esperada (5 clases).
    """
    output_shape = loaded_model.output_shape
    assert output_shape[-1] == EXPECTED_OUTPUT_SHAPE, \
        f"La forma de salida esperada es {EXPECTED_OUTPUT_SHAPE} (clases), pero se encontró {output_shape[-1]}"

def test_05_prediction_output(loaded_model):
    """
    Verifica que las predicciones generen una salida con la forma correcta.
    También asegura que la entrada se reforme a (muestras, 187, 1) antes de predecir.
    """
    # Generamos datos simulados con 187 características
    raw_data = np.random.rand(SAMPLE_SIZE, EXPECTED_TIMESTEPS).astype(np.float32)
    
    # Reformamos los datos para que coincidan con la entrada de la CNN: (muestras, 187, 1)
    simulated_data = raw_data.reshape(SAMPLE_SIZE, EXPECTED_TIMESTEPS, EXPECTED_CHANNELS)
    
    # Realiza la predicción
    predictions = loaded_model.predict(simulated_data, verbose=0)
    
    # Verifica que la forma de la salida sea (10 muestras, 5 clases)
    assert predictions.shape == (SAMPLE_SIZE, EXPECTED_OUTPUT_SHAPE), \
        f"La forma de las predicciones esperada es ({SAMPLE_SIZE}, {EXPECTED_OUTPUT_SHAPE}), pero se obtuvo {predictions.shape}"
