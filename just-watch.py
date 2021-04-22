from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
import time
import bs4
from bs4 import BeautifulSoup
from hdfs import InsecureClient

url = 'https://www.justwatch.com/es/proveedor/'
plataformas = ['amazon-prime-video', 'netflix', 'disney-plus', 'hbo']

def main(url, plataforma):
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
    # df =  pd.DataFrame.from_dict(data)
    # Exportación a csv
    # path = 'data/' + plataforma + '.csv' 
    # return df.to_csv(path_or_buf = path, index = False)
    return pd.DataFrame.from_dict(data)
# Para cada plataforma scroleamos y scrapeamos la pagina
client = InsecureClient('https://host:port')
for plataforma in plataformas:
    path = 'datalake/' + plataforma + '.csv' 
    url_plataforma = url + plataforma
    with client_hdfs.write(hdfs_path = path) as writer:
        main(url_plataforma, plataforma).to_csv(writer)


  