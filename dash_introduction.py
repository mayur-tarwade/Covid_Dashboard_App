import pandas as pd
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc

data = pd.read_csv(r'C:\Users\tarwa\OneDrive\Desktop\Data Science\Projects\Dash Applications\gapminder.csv')
app = dash.Dash()

app.layout = html.Div([
    html.Div(children=[
        html.H1('ANALYSIS DASHBOARD',style={'color':'white','text-align':'center','margin':'5px','padding':'5px'})
    ],style={'border':'1px black solid', 'float':'left','width':'100%', 'height':'50px','background':'#07575B'}),
    html.Div(children=[
        dcc.Graph(id='Scatter Plot',
                  figure={'data':[go.Scatter(x=data['pop'],
                                             y=data['gdpPercap'],
                                             mode='markers')],
                          'layout':go.Layout(title='Scatter Plot',
                                             xaxis={'title':'Pop'},
                                             yaxis={'title':'gdp/cap'})})
    ],style={'border':'1 px black solid', 'float':'left','width':'50%', 'height':'490px','background':'#003B46'}),
    html.Div(children=[
        dcc.Graph(id='Bar Plot',
                  figure={'data':[go.Bar(x=data['year'],
                                         y=data['pop'],
                                         marker={'color':'blue'},
                                         name='country')],
                          'layout':go.Layout(title='Bar Plot',
                                             xaxis={'title':'Year'},
                                             yaxis={'title':'Pop'})})
    ],style={'border':'1px black solid', 'float':'left','width':'49.70%', 'height':'490px','background':'#003B46'}),
html.Div(children=[
        dcc.Graph(id='Box Plot',
                  figure={'data':[go.Box(x=data['gdpPercap'])],
                          'layout':go.Layout(title='Box Plot')})
    ],style={'border':'1px black solid', 'float':'left','width':'50%', 'height':'490px','background':'#003B46'}),
])


if __name__== '__main__':
    app.run_server(debug=True)
