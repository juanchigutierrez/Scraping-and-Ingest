# Scraping-and-Ingest
Python Code Challenge
# Proyecto de Scraping y Almacenamiento en BigQuery

Este proyecto realiza scraping de datos desde una página web de noticias y almacena la información extraída en Google BigQuery. El proyecto está preparado para ejecutarse dentro de un contenedor Docker y ser desplegado en Google Cloud Run.

## Funcionalidades

1. **Scraping de datos web**: 
   - Extrae el título, la imagen, el enlace del artículo, y el primer párrafo de la noticia más destacada desde un sitio web.
   - Procesa la información para calcular el número de palabras y caracteres en el título, así como una lista de palabras capitalizadas que contiene el título.

2. **Almacenamiento en BigQuery**: 
   - Guarda los datos extraídos en una tabla de BigQuery.
   - Soporte para exportar los datos a un archivo CSV local.

## Estructura del Proyecto

- **`funciones_scraping.py`**: Contiene funciones principales para la extracción de datos desde la web, creación de un DataFrame, y almacenamiento de datos en BigQuery.
- **`main.py`**: Script principal que ejecuta el flujo de scraping y almacenamiento de datos.
- **`Dockerfile`**: Archivo de configuración para la creación del contenedor Docker que ejecuta el script.
- **`credenciales.json`**: Archivo de credenciales para autenticar con Google Cloud (BigQuery).
- **`deploy.sh`**: Script que despliega el contenedor en Google Cloud Run.
- **`requirements.txt`**: Archivo que especifica las dependencias del proyecto.

## Requisitos

- **Google Cloud**:
  - Tener una cuenta en Google Cloud con acceso a BigQuery.
  - Crear un servicio de cuenta en Google Cloud y descargar el archivo de credenciales JSON.
  - Activar la API de BigQuery y Cloud Run.
  
- **Local**:
  - Docker instalado.
  - Un archivo `credenciales.json` para acceder a Google Cloud.

## Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanchigutierrez/Scraping-and-Ingest.git
cd Scraping-and-Ingest
```

### 2. Configurar las credenciales de Google Cloud

Asegúrate de que el archivo `credenciales.json` esté ubicado en la carpeta raíz del proyecto o en la ubicación correcta y se encuentre bien referenciado en el archivo `deploy.sh` y en el `Dockerfile`.

### 3. Construir y ejecutar el contenedor Docker localmente

1. **Construir el contenedor**:

```bash
docker build -t nombre-imagen .
```

2. **Ejecutar el contenedor**:

```bash
docker run -it --rm -e GOOGLE_APPLICATION_CREDENTIALS="/app/credenciales.json" nombre-imagen
```

Esto ejecutará el script y realizará el scraping en el sitio web especificado.

### 4. Desplegar en Google Cloud Run

Si prefieres ejecutar la aplicación en la nube, puedes usar el script `deploy.sh` para realizar el despliegue en Google Cloud Run.

1. **Asegúrate de que tus credenciales estén correctamente configuradas**:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="./credenciales.json"
```

1. **Ejecuta el script de despliegue**:

```bash
./deploy.sh
```
Esto desplegará el contenedor en Google Cloud Run, donde será accesible a través de una URL.

## BigQuery

El proyecto incluye una función para almacenar los resultados directamente en una tabla de Google BigQuery. Asegúrate de configurar correctamente los siguientes valores al llamar la función `guardar_en_bigquery`:

```bash
fs.guardar_en_bigquery(df, project_id='proyecto-id', dataset_id='dataset', table_id='tabla')
```
### Parámetros:

- `project_id`: El ID de tu proyecto de Google Cloud.

- `dataset_id`: El nombre del dataset en BigQuery.

- `table_id`: El nombre de la tabla donde se almacenarán los datos.

## Dependencias

Las dependencias de Python están especificadas en el archivo `requirements.txt`. Para instalarlas localmente, puedes usar `pip`:

```bash
pip install -r requirements.txt
```

## Notas adicionales

- **Cerrar el navegador**: Prestar especial atención a la función `driver.quit()` para cerrar el navegador y evitar que el proceso quede abierto después de realizar el scraping.

- **Credenciales de Google Cloud**: Asegúrate de que las credenciales de Google Cloud estén configuradas correctamente antes de ejecutar el script o desplegarlo en Cloud Run.
