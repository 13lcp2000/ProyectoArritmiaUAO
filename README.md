# Predicción de Episodios de Arritmia Cardíaca  
**Proyecto Arritmia UAO**

---

## ✨ Introducción

Este repositorio contiene una aplicación desarrollada en **Streamlit** para la **clasificación y predicción de arritmias cardíacas**, utilizando un modelo previamente entrenado y empaquetado en formato **MLflow**.

El despliegue se realiza de manera sencilla y reproducible mediante **Docker**, garantizando que el entorno de ejecución (Python 3.11, TensorFlow, Streamlit, MLflow, etc.) sea idéntico en cualquier equipo, sin importar el sistema operativo.

📌 **Estado actual:**  
El proyecto se encuentra **estable, funcional y desplegable completamente dentro de su contenedor Docker (versión v4).**

---

## 🐳 Despliegue rápido con Docker

Sigue estos tres pasos para tener la aplicación corriendo en tu máquina en pocos minutos.

### 🔧 Requisitos previos
Asegúrate de tener **Docker** instalado y en ejecución  
(en **Windows**, **macOS** o **Linux**).

---

### 🧱 Paso 1 – Construir la imagen (Build)

Desde la carpeta raíz del proyecto (`ProyectoArritmiaUAO`), donde se encuentra el archivo `Dockerfile`, ejecuta el siguiente comando:

```bash
docker build -t proyectoarritmias:v4 .
⏱️ Nota:
La primera construcción puede tardar varios minutos, ya que instala todas las librerías dentro del contenedor (TensorFlow, MLflow, Streamlit, etc.).

▶️ Paso 2 – Ejecutar el contenedor (Run)
Inicia el contenedor en modo detached (-d) y mapea el puerto 8501 de Streamlit:

bash
Copiar código
docker run -d --name arritmia-app -p 8501:8501 proyectoarritmias:v4
🌐 Paso 3 – Acceder a la aplicación
Abre tu navegador y dirígete a:

👉 http://localhost:8501

La aplicación se cargará lista para recibir un archivo CSV sin encabezados (188 columnas numéricas)
y generar la predicción en tiempo real.

 Modelo en formato MLflow
El modelo fue convertido desde un archivo Keras (PrediccionArritmia.keras) a formato MLflow, utilizando el script:

bash
Copiar código
python save_mlflow_model.py
Esto permite una mejor portabilidad, versionamiento y compatibilidad con herramientas de seguimiento de experimentos.

El modelo final se encuentra dentro de:
📁 src/modelo_mlflow/

🧹 Limpieza del entorno Docker
Si necesitas detener o eliminar el contenedor:

bash
Copiar código
# Detener el contenedor en ejecución
docker stop arritmia-app

# Eliminar el contenedor detenido
docker rm arritmia-app

# (Opcional) Eliminar la imagen para liberar espacio
docker rmi proyectoarritmias:v4
También puedes realizar una limpieza general del entorno:

bash
Copiar código
docker system prune -f

👨‍💻 Autores
María Alejandra Niño
Pablo Moreno
Leonardo Collazos
Juan Guillermo Restrepo Morales

Estudiantes de la Especialización en Inteligencia Artificial – Universidad Autónoma de Occidente (UAO)
📍 Cali, Colombia