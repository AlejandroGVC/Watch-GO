from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
import time
import bs4
from bs4 import BeautifulSoup

url = 'https://www.justwatch.com/es/proveedor/'
plataformas = ['amazon-prime-video', 'netflix', 'disney-plus', 'hbo']

def main(url, plataforma):
    '''
    Devuelve un dataframe con el nombre del proveedor de
    servicio streaming, si es una serie o pelicula y 
    el titulo
    '''
    driver = webdriver.Safari()
    driver.get(url)
    # Scrolea la pagina hasta el final, y no para hasta que no paran de generarse
    # nuevas peliculas o series
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    ##
    html = driver.page_source
    driver.close()
    ## A partir de aqui el scrapeo se hace con bs4 para que sea mas rapido
    html = BeautifulSoup(html, 'html.parser')
    titulos = html.find_all('div', {'class':'title-list-grid__item'})
    links = []
    for titulo in titulos:
        links.append(titulo.find('a').get('href'))
    # Creacion del DF
    data = {'Plataforma':[],'Tipo':[], 'Titulo':[]}
    for link in links:
        data['Plataforma'].append(plataforma)
        data['Tipo'].append(link.split('/')[-2])
        data['Titulo'].append(link.split('/')[-1].replace('-', ' '))
    return pd.DataFrame.from_dict(data)
# Union de los dataframes
df_final = []
for plataforma in plataformas:
    df = main(url + plataforma, plataforma)
    df_final.append(df)
df_final = pd.concat(df_final)
# Escritura
df_final.to_csv('data/just-watch.csv', index=False)



  