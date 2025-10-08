import tensorflow as tf
import mlflow.keras
import os

# --- Configuración ---
KERAS_MODEL_PATH = "src/modelo/PrediccionArritmia.keras"
MLFLOW_MODEL_PATH = "src/modelo_mlflow"

def save_model_to_mlflow():
    """Carga el modelo Keras y lo guarda en formato MLflow."""
    print(f"1. Cargando modelo desde: {KERAS_MODEL_PATH}")

    if not os.path.exists(KERAS_MODEL_PATH):
        print(f"ERROR: No se encontró el modelo en la ruta esperada: {KERAS_MODEL_PATH}")
        return

    # Cargar el modelo Keras
    try:
        model = tf.keras.models.load_model(KERAS_MODEL_PATH)
    except Exception as e:
        print(f"ERROR al cargar el modelo con Keras: {e}")
        return

    print("2. Modelo cargado exitosamente.")

    # Crear carpeta de destino si no existe
    os.makedirs(MLFLOW_MODEL_PATH, exist_ok=True)

    # Guardar el modelo en formato MLflow (sin keras_module)
    mlflow.keras.save_model(
        model,
        MLFLOW_MODEL_PATH
    )

    print(f"\n✅ Modelo guardado en formato MLflow en: {MLFLOW_MODEL_PATH}/")
    print("   El archivo .keras original ahora está empaquetado y listo para ser cargado por MLflow.")

if __name__ == "__main__":
    save_model_to_mlflow()
