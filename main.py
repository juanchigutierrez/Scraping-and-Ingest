import funciones_scraping as fs

website = 'https://www.yogonet.com/international/'
path = r'C:\Users\emili\Desktop\codigo_juanchi\chromedriver-win64\chromedriver.exe'

driver = fs.iniciar_driver(path)

try:
    title, image_url, article_url, first_paragraph = fs.extraer_datos(driver, website)

    if title:
        df = fs.crear_dataframe(title, image_url, article_url, first_paragraph)
        print(df)
        # fs.guardar_csv(df)

finally:
    driver.quit()
