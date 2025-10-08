# Usa una imagen base de Python oficial, ligera y con versión 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala uv para gestionar dependencias rápidamente
RUN pip install uv

# Copia los archivos de configuración de dependencias y el código fuente
COPY requirements.txt .
COPY src /app/src

# Instala todas las dependencias dentro del contenedor usando uv
RUN uv pip install --system -r requirements.txt

# Copia el modelo en formato MLflow (no el Keras original)
COPY src/modelo_mlflow /app/src/modelo_mlflow

# Exponer el puerto por defecto de Streamlit (8501)
EXPOSE 8501

# Definir la instrucción de inicio de la aplicación
# Usamos 'uv run' para iniciar Streamlit, asegurando entorno limpio
CMD ["uv", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
