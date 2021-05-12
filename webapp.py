import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv('data/just-watch.csv')

app.layout = html.Div([
    html.H1("Watch&Go", style = {'text-align':'center'}),
    
    dcc.Input(
        id='search',
        placeholder='Busca una pelicula o serie...',
        type='text',
        value='inception'
    ),
    
    html.Div(
        id='output_container',
        children = [] #aqui iran las peliculas 
    )
    
    
])

@app.callback(
    Output(component_id='output_container', component_property='children'),
    [Input(component_id='search', component_property='value')]
)

def show_movies(movie):
    
    dff = df.copy()
    
    movie_selected = dff[dff['Titulo'] == movie]
    
    return movie_selected

if __name__ == '__main__':
    app.run_server(debug=True)