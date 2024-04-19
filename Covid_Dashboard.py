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


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)


if __name__ == '__main__':
    app.run_server(debug=True)
