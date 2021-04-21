from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
import time

url = 'https://www.justwatch.com/es/proveedor/amazon-prime-video'

def main(url, plataforma):
    driver = webdriver.Safari()
    driver.get(url)
    # Scrolea la pagina hasta el final, y no para hasta que no paran de generarse
    # nuevas peliculas o series
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    ##
    titulos = driver.find_elements(By.CLASS_NAME, 'title-list-grid__item--link')
    links = []
    for titulo in titulos:
        links.append(titulo.get_attribute('href'))
    driver.close()
    # Creacion del DF
    data = {'Plataforma':[],'Tipo':[], 'Titulo':[]}
    for link in links:
        data['Plataforma'].append(plataforma)
        data['Tipo'].append(link.split('/')[-2])
        data['Titulo'].append(link.split('/')[-1].replace('-', ' '))
    df =  pd.DataFrame.from_dict(data)
    # Exportación a csv
    path = 'data/' + plataforma + '.csv' 
    return df.to_csv(path_or_buf = path, index = False)

main(url, 'prime_video')