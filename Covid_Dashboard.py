import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc
from dash import Input,Output

# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

patients = pd.read_csv(r'C:\Users\tarwa\OneDrive\Desktop\Data Science\Projects\Dash Applications\Datasets\IndividualDetails.csv')
total = patients.shape[0]
active = patients[patients['current_status']== 'Hospitalized'].shape[0]
recovered = patients[patients['current_status']== 'Recovered'].shape[0]
deaths = patients[patients['current_status']== 'Deceased'].shape[0]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.layout=html.Div(children=[
    html.H1("Covid Pandemic Dashboard - India's Perspective"),
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H3('Total Cases', className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H3('Active Cases', className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H3('Recovered', className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3'),
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H3('Deaths', className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3')
    ], className='row'),

    html.Div(children=[
        html.Div(children=[], className='col-md-6'),
        html.Div(children=[], className='col-md-6'),
    ], className='row'),

    html.Div(children=[
        html.Div(children=[], className='col-md-12'),
    ], className='row'),

], className='container')





if __name__ == '__main__':
    app.run_server(debug=True)
