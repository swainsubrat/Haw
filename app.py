import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import io
import base64
from Dependencies.PlotBuilder import MessageFigurePlotter, EmojiFigurePlotter
from Dependencies.DataFrameBuilder import (messageDataFrameBuilder,
                                           emojiDataFrameBuilder)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.title = 'Haw 🤗'

app.layout = html.Div([
    html.H1(
        'Haw',
        style={
            'textAlign': 'center',
            'font-weight': 'bold'
        }
    ),

    html.Div(
        'Haw: Heavily Analysed Whatsapp texts', 'value',
        style={
            'textAlign': 'center',
        }
    ),

    html.Hr(),

    dcc.Upload(
        html.Button('Upload File'),
        id='upload-data',
        style={'textAlign': 'center'}
    ),

    html.Div(id='graphm', children=[]),
    html.Div(id='graphe', children=[])
])


def parse_message(content, name, date):
    _, content_string = content.split(',')
    FILE_NAME = name
    decoded = base64.b64decode(content_string)
    f = io.StringIO(decoded.decode('utf-8'))
    DFM = messageDataFrameBuilder(FILE=f)
    FIGM = MessageFigurePlotter(DFM=DFM, group_name=FILE_NAME.split(".")[0])

    return FIGM


def parse_emoji(content, name, date):
    _, content_string = content.split(',')
    FILE_NAME = name
    decoded = base64.b64decode(content_string)
    f = io.StringIO(decoded.decode('utf-8'))
    DFE = emojiDataFrameBuilder(FILE=f)
    FIGE = EmojiFigurePlotter(DFE=DFE, group_name=FILE_NAME.split(".")[0])

    return FIGE


@app.callback(Output('graphm', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_message_plots(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        child = parse_message(
            content=list_of_contents,
            name=list_of_names,
            date=list_of_dates
        )
        return child['barm'], child['barD'], child['barY'],\
            child['piem']


@app.callback(Output('graphe', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_emoji_plots(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        child = parse_emoji(
            content=list_of_contents,
            name=list_of_names,
            date=list_of_dates
        )
        return child['piee'], child['bare'], child['pieeg'],\
            child['bareg'], child['bareD'], child['bareY']


if __name__ == '__main__':
    app.run_server(debug=True)
