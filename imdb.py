import pandas as pd
import zipfile
#import subprocess

#Descarga dataset por terminal
#cmd = 'kaggle datasets download stefanoleone992/imdb-extensive-dataset  -f IMDB Movies.csv'
#subprocess.run(cmd)

# Hace el unzip 
zip = zipfile.ZipFile('data/IMDb%20movies.csv.zip')
zip.extractall('data')


