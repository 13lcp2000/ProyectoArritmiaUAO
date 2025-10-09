🫀 Predicción de Episodios de Arritmia Cardíaca
Proyecto Arritmia UAO
✨ Introducción y Arquitectura
Este proyecto contiene una aplicación desarrollada en Streamlit para la clasificación y predicción de arritmias cardíacas.

El modelo de predicción fue estandarizado utilizando MLflow para asegurar:

Portabilidad: El modelo se carga en un formato universal (src/modelo_mlflow/).

Trazabilidad: Se puede registrar el proceso de entrenamiento en el Servidor de Seguimiento de MLflow.

El despliegue se realiza de manera sencilla y reproducible mediante Docker, garantizando que el entorno de ejecución (Python 3.11, TensorFlow, MLflow, etc.) sea idéntico en cualquier sistema operativo.

Estado Actual:
El proyecto está estable, funcional y desplegable completamente dentro de su contenedor Docker (versión v4).

🐳 Despliegue Rápido con Docker
Sigue estos tres sencillos pasos para tener la aplicación corriendo en tu máquina en pocos minutos.

🔧 Requisitos Previos
Asegúrate de tener Docker instalado y en ejecución en tu sistema (Windows, macOS o Linux).

🧱 Paso 1 – Construir la Imagen (Build)
Desde la carpeta raíz del proyecto (ProyectoArritmiaUAO), donde se encuentra el Dockerfile, ejecuta el siguiente comando:

docker build -t proyectoarritmias:v4 .

Nota: La primera construcción puede tardar varios minutos, ya que instala todas las librerías necesarias dentro del contenedor.

▶️ Paso 2 – Ejecutar el Contenedor (Run)
Inicia el contenedor en modo detached (-d), asígnale el nombre arritmia-app y mapea el puerto 8501 de Streamlit:

docker run -d --name arritmia-app -p 8501:8501 proyectoarritmias:v4

🌐 Paso 3 – Acceder a la Aplicación
Abre tu navegador y dirígete a:

👉 http://localhost:8501

La aplicación Streamlit se cargará lista para recibir un archivo CSV (188 columnas numéricas sin encabezados) y generar la predicción.

🧹 Limpieza y Mantenimiento de Docker
Para detener y eliminar el contenedor o liberar recursos después de usar la aplicación:

# Detener el contenedor en ejecución
docker stop arritmia-app

# Eliminar el contenedor detenido
docker rm arritmia-app

# (Opcional) Eliminar la imagen para liberar espacio
# docker rmi proyectoarritmias:v4

👨‍💻 Autores
María Alejandra Niño

Pablo Moreno

Leonardo Collazos

Juan Guillermo Restrepo Morales

Estudiantes de la Especialización en Inteligencia Artificial – Universidad Autónoma de Occidente (UAO)
Cali, Colombia
