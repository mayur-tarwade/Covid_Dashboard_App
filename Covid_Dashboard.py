import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc
from dash import Input,Output
import streamlit as st

# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
# Datasets import:
patients = pd.read_csv('Datasets/IndividualDetails.csv')
total = patients.shape[0]
active = patients[patients['current_status']== 'Hospitalized'].shape[0]
recovered = patients[patients['current_status']== 'Recovered'].shape[0]
deaths = patients[patients['current_status']== 'Deceased'].shape[0]

D_patients = patients[patients['nationality'] == 'India']

dbd = pd.read_csv('Datasets/covid_19_india.csv')
age = pd.read_csv('Datasets/AgeGroupDetails.csv')

options=[
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'}
]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)
server = app.server

# Application Layout:
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
        html.Div(children=[
            html.Div([
                html.Div([
                    html.H5('Scatter Plot',className='text-light',style={'text-align':'center'}),
                    dcc.Graph(id='Scatter Plot',
                              figure={'data':[go.Scatter(x=dbd['Date'],
                                                         y=dbd['Confirmed'],
                                                         mode='markers',text=dbd['State/UnionTerritory'])],
                                      'layout':go.Layout(title='Day by Day Analysis',
                                                         xaxis={'title':'Date'},
                                                         yaxis={'title':'No. Of Patients'})})
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-6'),
        html.Div(children=[
            html.Div([
                html.Div([
                    html.H5('Pie Chart',className='text-light',style={'text-align':'center'}),
                    dcc.Graph(id='Pie Chart',
                              figure={'data':[go.Pie(labels=age['AgeGroup'],values=age['TotalCases'])],
                                      'layout':go.Layout(title='Age Contribution')})
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-6'),
    ], className='row'),

    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H4('Current Status of State Analysis',className='text-light', style={'text-align':'center'}),
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-12'),
    ], className='row'),
], className='container')

# @app.callback- decorator
@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):
    if type=='All':
        pbar = patients['detected_state'].value_counts().reset_index()
        return {'data':[go.Bar(x=pbar['detected_state'], y=pbar['count'])],
                'layout':go.Layout(title='State Total Count')}
    else:
        npat = patients[patients['current_status'] == type]
        pbar = npat['detected_state'].value_counts().reset_index()
        return {'data':[go.Bar(x=pbar['detected_state'], y=pbar['count'])],
                'layout':go.Layout(title=type)}

if __name__ == '__main__':
    app.run_server(debug=True)

