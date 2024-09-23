from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas as pd
# from google.cloud import bigquery
# import pandas_gbq

# URL de la página a visitar
website = 'https://www.yogonet.com/international/'
# Ruta al ejecutable de ChromeDriver
path = r'C:\Users\emili\Desktop\codigo_juanchi\chromedriver-win64\chromedriver.exe'

# Comprobar si la ruta de ChromeDriver existe
if not os.path.exists(path):
    raise FileNotFoundError(f"ChromeDriver no encontrado en la ruta: {path}")

# Crear un objeto Service
service = Service(executable_path=path)

# Crear una nueva instancia del controlador Chrome usando el objeto Service
driver = webdriver.Chrome(service=service)

try:
    # Abrir la página web
    driver.get(website)

    # Espera hasta que el contenedor esté presente
    contenedor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "contenedor_modulo.noticias_publicidad_destacadas"))
    )

    # Encuentra el primer título (h2)
    title = contenedor.find_element(By.TAG_NAME, "h2").text
    print(f"Primer Título: {title}")

    # Encuentra la primera imagen (usualmente en una etiqueta <img>)
    try:
        image_element = contenedor.find_element(By.TAG_NAME, "img")
        image_url = image_element.get_attribute('src')
    except:
        image_url = "No se encontró la imagen"

    print(f"Primera Imagen: {image_url}")

    # Extraer el enlace (asumiendo que está en una etiqueta <a> que envuelve el título)
    try:
        link_element = contenedor.find_element(By.TAG_NAME, "a")
        article_url = link_element.get_attribute('href')
    except:
        article_url = "No se encontró el enlace"
    print(f"Primer Enlace: {article_url}")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()

# Post-proceso: análisis del título
word_count = len(title.split())  # Recuento de palabras en el título
char_count = len(title)  # Recuento de caracteres en el título
capitalized_words = [word for word in title.split() if word.istitle()]  # Palabras en mayúsculas

# Crear un DataFrame con la información obtenida
data = {
    'Título': [title],
    # 'Kicker': [kicker],
    'URL de la imagen': [image_url],
    'Enlace del artículo': [article_url],
    'Recuento de palabras en el título': [word_count],
    'Recuento de caracteres en el título': [char_count],
    'Palabras que comienzan con mayúscula': [capitalized_words]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Guardar el DataFrame en un archivo CSV (si lo necesitas)
# df.to_csv('resultados.csv', index=False)