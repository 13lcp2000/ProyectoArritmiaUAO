🫀 Predicción de Episodios de Arritmia Cardíaca
Proyecto Arritmia UAO
✨ Introducción

Este repositorio contiene una aplicación desarrollada en Streamlit para la clasificación y predicción de arritmias cardíacas utilizando un modelo de Keras preentrenado.

El despliegue se realiza de forma sencilla y reproducible mediante Docker, asegurando que el entorno de ejecución (Python 3.11, TensorFlow, Streamlit, etc.) sea idéntico en cualquier equipo.

📌 Estado actual: Proyecto estable y completamente funcional dentro de su contenedor Docker.

🐳 Despliegue Rápido con Docker

Sigue estos tres pasos para tener la aplicación corriendo en tu máquina en pocos minutos.

🔧 Requisitos previos

Asegúrate de tener Docker instalado y en ejecución (ya sea en Windows, macOS o Linux).

Paso 1 – Construir la imagen (Build)

Desde la carpeta raíz del proyecto (ProyectoArritmiaUAO), donde se encuentra el Dockerfile, ejecuta el siguiente comando para construir la imagen.
Usaremos la etiqueta v2 para indicar la versión estable.

docker build -t proyectoarritmias:v2 .


⏱️ Nota: Este proceso puede tardar varios minutos la primera vez, ya que instala todas las librerías necesarias dentro del contenedor (incluyendo TensorFlow y Keras).

Paso 2 – Ejecutar el contenedor (Run)

Una vez construida la imagen, inicia el contenedor en modo detached (-d) y mapea el puerto interno de Streamlit (8501) a tu puerto local:

docker run -d -p 8501:8501 --name arritmias_app_v2 proyectoarritmias:v2

Paso 3 – Acceder a la aplicación

Abre tu navegador y dirígete a:

👉 http://localhost:8501

La aplicación Streamlit se cargará lista para recibir un archivo CSV de prueba y generar una predicción en tiempo real.

📂 Estructura del Proyecto
Archivo / Carpeta	Propósito	Descripción
Dockerfile	Definición del entorno	Define la imagen base (python:3.11-slim) e instala las dependencias necesarias. Además, asegura la ruta correcta del modelo (src/modelo/).
requirements.txt	Dependencias	Lista las librerías de Python requeridas (Streamlit, TensorFlow, pandas, etc.).
src/app.py	Aplicación principal	Contiene la interfaz Streamlit y la lógica de predicción. Utiliza la ruta src/modelo/PrediccionArritmia.keras para cargar el modelo dentro del contenedor.
src/modelo/	Modelo Keras	Carpeta donde se encuentra el archivo binario del modelo (PrediccionArritmia.keras).
🧹 Limpieza del Entorno Docker

Si necesitas detener la aplicación o liberar el puerto (8501), puedes ejecutar los siguientes comandos:

# Detener el contenedor en ejecución
docker stop arritmias_app_v2

# Eliminar el contenedor detenido
docker rm arritmias_app_v2

# (Opcional) Eliminar la imagen para liberar espacio
# docker rmi proyectoarritmias:v2

👨‍💻 Autores

Maria Alejandra Niño, Pablo Moreno,Leonardo Collazos, Juan Guillermo Restrepo
Estudiantes de Especialización en Inteligencia Artificial – Universidad Autónoma de Occidente (UAO)
Cali, Colombia