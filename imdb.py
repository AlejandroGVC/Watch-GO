import pandas as pd
import zipfile

# Descarga dataset por terminal
#cmd = 'kaggle datasets download stefanoleone992/imdb-extensive-dataset  -f IMDB\ Movies.csv -p data'

# Hace el unzip y crea un dataframe
zip = zipfile.ZipFile('data/IMDb%20movies.csv.zip')
zip.extractall('data')
df = pd.read_csv('data/IMDb movies.csv')

