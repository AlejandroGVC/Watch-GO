import pandas as pd
import zipfile
from hdfs import InsecureClient

# Descarga dataset por terminal
#cmd = 'kaggle datasets download stefanoleone992/imdb-extensive-dataset  -f IMDB\ Movies.csv -p data'

# Hace el unzip y crea un dataframe
zip = zipfile.ZipFile('data/IMDb%20movies.csv.zip')
zip.extractall('data')
df = pd.read_csv('data/IMDb movies.csv')

# Creacion del entorno hdfs y escritura del fichero en csv
client = InsecureClient('http://host:port', user='ann')
with client_hdfs.write('datalake/imdb.csv',) as writer:
	df.to_csv(writer)