import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from hdfs import InsecureClient

url = 'https://www.filmaffinity.com/es/cat_new_th_es.html'

def get_html(url):
	# Devuelve el contenido del html en un objeto beaufitul soup
	page = requests.get(url)
	return BeautifulSoup(page.content, 'html.parser')

def main(url):
	peliculas = get_html(url).find_all('div', {'class':'movie-title'})
	ls_links_movie = []
	ls_link_cine = []
	ls_link = []
	data = []
	for pelicula in peliculas:
		ls_links_movie.append(pelicula.find('a').get('href'))
	for url_peli in ls_links_movie:
		#criticas
		#año, ...
		tabs = get_html(url_peli).find('ul', {'class':'ntabs'}).find_all('a')
		for tab in tabs:
			ls_link_cine.append(tab.get('href') + str('&state=ES-M'))
	for link in ls_link_cine:
		if 'movie-showtimes' in link:
			ls_link.append(link)
	for url_cine in ls_link:
		pelicula = get_html(url_cine).find('h1', {'id':'main-title'}).text
		dict_ = {'Pelicula': pelicula, 'Cines':[]}
		ls_cines = get_html(url_cine).find_all('div', {'class':'th-name'})
		for cine in ls_cines:
			nombre_cine = cine.text
			dict_['Cines'].append(nombre_cine)
		data.append(dict_)
	return pd.DataFrame.from_dict(data)
# Creacion del entorno hdfs y escritura del fichero en csv
client = InsecureClient('http://host:port', user='ann')
with client_hdfs.write('datalake/cartelera.csv',) as writer:
	main(url).to_csv(writer)
