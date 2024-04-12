import pandas as pd
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc

data = pd.read_csv(r'C:\Users\tarwa\OneDrive\Desktop\Data Science\Projects\Dash Applications\gapminder.csv')
app = dash.Dash()

app.layout = html.Div([
    html.Div(children=[
        html.H1('First Dashboard', style={'color':'orange', 'text-align':'center','margin':'5px','padding':'5px'})
    ],style={'border':'1px black solid', 'float':'left','width':'100%', 'height':'50px'}),
    html.Div(style={'border':'1px black solid', 'float':'left','width':'50%', 'height':'350px'}),
    html.Div(style={'border':'1px black solid', 'float':'left','width':'49.70%', 'height':'350px'}),
])

if __name__== '__main__':
    app.run_server(debug=True)