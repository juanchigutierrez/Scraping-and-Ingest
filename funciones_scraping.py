from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd

def iniciar_driver(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"ChromeDriver no encontrado en la ruta: {path}")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    return driver

def extraer_datos(driver, website):
    driver.get(website)

    try:
        # Esperar hasta que el contenedor esté presente
        contenedor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "contenedor_modulo.noticias_publicidad_destacadas"))
        )

        # Extraer el primer título (h2)
        title = contenedor.find_element(By.TAG_NAME, "h2").text

        # Extraer la primera imagen
        try:
            image_element = contenedor.find_element(By.TAG_NAME, "img")
            image_url = image_element.get_attribute('src')
        except:
            image_url = "No se encontró la imagen"

        # Extraer el enlace del artículo
        try:
            link_element = contenedor.find_element(By.TAG_NAME, "a")
            article_url = link_element.get_attribute('href')
        except:
            article_url = "No se encontró el enlace"
        
        # Hacer clic en el título para ir a la página del artículo
        try:
            link_element.click()
            
            # Esperar hasta que el artículo cargue, buscando el div que contiene el contenido de la noticia
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inner_contenido_noticia.fuente_open_sans"))
            )
            
            # Buscar el div con la clase específica y extraer el primer párrafo dentro de ese div
            try:
                content_div = driver.find_element(By.CLASS_NAME, "inner_contenido_noticia.fuente_open_sans")
                first_paragraph = content_div.find_element(By.TAG_NAME, "p").text
            except:
                first_paragraph = "No se encontró el primer párrafo dentro del div especificado"
        
        except:
            first_paragraph = "No se pudo hacer clic en el título o cargar el artículo"

        return title, image_url, article_url, first_paragraph

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None, None, None, None

def crear_dataframe(title, image_url, article_url, first_paragraph):
    word_count = len(title.split()) if title else 0
    char_count = len(title) if title else 0
    capitalized_words = [word for word in title.split() if word.istitle()] if title else []

    data = {
        'Título': [title],
        'URL de la imagen': [image_url],
        'Enlace del artículo': [article_url],
        'Primer parrafo': [first_paragraph],
        'Recuento de palabras en el título': [word_count],
        'Recuento de caracteres en el título': [char_count],
        'Palabras que comienzan con mayúscula': [capitalized_words]
    }

    df = pd.DataFrame(data)
    return df

def guardar_csv(df, filename='resultados.csv'):
    df.to_csv(filename, index=False)
