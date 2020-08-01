import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import io
import base64
from Dependencies.PlotBuilder import FiguresPlotter
from Dependencies.DataFrameBuilder import DataFrameBuilder

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H1(
        'HAWW',
        style={
            'textAlign': 'center',
            # 'color': colors['text'],
            'font-weight': 'bold'
        }
    ),

    html.Div(
        'Hawww: An Analytics Tool Made for WhatsApp Groups', 'value',
        style={
            'textAlign': 'center',
            # 'color': colors['text']
        }
    ),

    html.Hr(),

    dcc.Upload(
        html.Button('Upload File'),
        id='upload-data',
        style={'textAlign': 'center'}
    ),

    html.Div(id='graph', children=[])
])


def parse_content(content, name, date):
    _, content_string = content.split(',')
    FILE_NAME = name
    decoded = base64.b64decode(content_string)
    f = io.StringIO(decoded.decode('utf-8'))
    DF = DataFrameBuilder(FILE=f)
    FIG = FiguresPlotter(DF=DF, group_name=FILE_NAME.split(".")[0])

    return FIG


@app.callback(Output('graph', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        child = parse_content(
            content=list_of_contents,
            name=list_of_names,
            date=list_of_dates
        )
        return child['barm'], child['barD'], child['barY'],\
            child['piem'], child['piee'], child['bare'], child['pieeg'],\
            child['bareg'], child['bareD'], child['bareY']


if __name__ == '__main__':
    app.run_server(debug=True)
