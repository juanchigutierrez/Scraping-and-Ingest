import funciones_scraping as fs

website = 'https://www.yogonet.com/international/'

# Llamada a la función sin necesidad de especificar la ruta del ChromeDriver
driver = fs.iniciar_driver()

try:
    title, image_url, article_url, first_paragraph = fs.extraer_datos(driver, website)

    if title:
        df = fs.crear_dataframe(title, image_url, article_url, first_paragraph)
        print(df)
        # fs.guardar_csv(df)

    # Llamar a la función para guardar en BigQuery
    fs.guardar_en_bigquery(df, project_id='proyecto-id', dataset_id='dataset', table_id='tabla')

finally:
    driver.quit()
