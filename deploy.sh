#!/bin/bash

# Variables de configuración
PROJECT_ID="proyecto-id"            # Cambiar esto por ID del proyecto
REGION="us-central1"                # Cambiar esto si usa otra región
SERVICE_NAME="nombre-servicio"      # Nombre del servicio en Cloud Run
IMAGE_NAME="nombre-imagen"          # Nombre de la imagen Docker
ARTIFACT_REGISTRY="gcr.io"          # Si usa Container Registry; cambiar a "artifactregistry.googleapis.com" si es Artifact Registry

# Nombre completo de la imagen
IMAGE_URL="$ARTIFACT_REGISTRY/$PROJECT_ID/$IMAGE_NAME"

# Ruta al archivo de credenciales
CREDENTIALS_PATH="./credenciales.json" 

# Configurar las credenciales
echo "Configurando autenticación con credenciales de Google Cloud..."
export GOOGLE_APPLICATION_CREDENTIALS="$CREDENTIALS_PATH"

# Autenticarse con Google Cloud
echo "Autenticando con Google Cloud..."
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

# Establecer el proyecto de Google Cloud
echo "Estableciendo el proyecto de Google Cloud..."
gcloud config set project $PROJECT_ID

# Construir la imagen de Docker
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Etiquetar la imagen para subirla al registro
echo "Etiquetando la imagen..."
docker tag $IMAGE_NAME $IMAGE_URL

# Subir la imagen a Google Container Registry o Artifact Registry
echo "Subiendo la imagen al registro de contenedores..."
docker push $IMAGE_URL

# Desplegar la imagen en Cloud Run
echo "Desplegando en Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_URL \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated

# Despliegue finalizado
echo "¡Despliegue completado con éxito!"
