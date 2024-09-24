# Usa una imagen base de Python 3.9
FROM python:3.9-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium-driver

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos
COPY requirements.txt requirements.txt

# Instalar las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Configurar la variable de entorno de Google BigQuery (credenciales)
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credenciales.json"

# Exponer el puerto
EXPOSE 8080

# Ejecutar el script de Python
CMD ["python", "main.py"]
