from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import pandas as pd
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.justwatch.com/es?providers=nfx'
driver = webdriver.Safari()
driver.get(url)

lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

titulos = driver.find_elements(By.CLASS_NAME, 'title-list-grid__item--link')

links = []
for titulo in titulos:
	links.append(titulo.get_attribute('href'))

data = {'Tipo':[], 'Titulo':[]}

for link in links:
	data['Tipo'].append(link.split('/')[-2])
	data['Titulo'].append(link.split('/')[-1].replace('-', ' '))
	
print(pd.DataFrame.from_dict(data))
driver.close()





