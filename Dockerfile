# Usa una imagen base de Python oficial, ligera y con version 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala uv para gestionar dependencias rápidamente
RUN pip install uv

# Copia los archivos de configuración de dependencias y el código
COPY requirements.txt .
COPY src /app/src

# Instala todas las dependencias usando uv dentro del contenedor
RUN uv pip install --system -r requirements.txt

# Copia los assets adicionales (el modelo Keras) a la ruta esperada.
# La aplicación buscará el modelo en /app/src/modelo/PrediccionArritmia.keras
COPY src/modelo /app/src/modelo

# Exponer el puerto por defecto de Streamlit (8501)
EXPOSE 8501

# Definir la instrucción de inicio
# Usamos 'uv run' para iniciar Streamlit
CMD ["uv", "run", "streamlit", "run", "src/app.py"]