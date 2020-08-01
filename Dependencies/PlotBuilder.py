"""
Creates plots for the webapp
"""

import dash_core_components as dcc
import plotly.express as px

from .PlotlyViz import PlotlyViz
from plotly.graph_objs._figure import Figure
from dash_core_components import Graph


def _wrapper(fig: Figure, id: str) -> Graph:
    return dcc.Graph(
        figure=fig,
        id=id
    )


def MessageFigurePlotter(DFM: dict,
                         group_name: str) -> dict:
    """
    Function to plot the plots for message statistics.

    Args:
        DFM(dict): Dict of dataframes containing message statistics.
        group_name: WhatsApp group name.

    Returns:
        FIGM(dict(Figure)): Dictionary of Plotly's figure objects.
    """
    instance = PlotlyViz(df=DFM['dfm'])
    bar = instance.bar_plot(
        x='Name', y='Message Count',
        title='Message count of {}'.format(group_name),
        text='Message Count'
    )
    pie = instance.pie_plot(
        values='Message Count',
        groupby='Name',
        title='Message Contribution Plot',
        color_discrete_sequence=px.colors.sequential.Plotly3
    )
    barm = _wrapper(fig=bar, id='figm')
    piem = _wrapper(fig=pie, id='piem')

    instance = PlotlyViz(df=DFM['dfmD'])
    bar = instance.bar_plot(
        x="Date", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barD = _wrapper(fig=bar, id='barD')

    instance = PlotlyViz(df=DFM['dfmMY'])
    bar = instance.bar_plot(
        x="Month_Year", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barMY = _wrapper(fig=bar, id='barMY')

    instance = PlotlyViz(df=DFM['dfmY'])
    bar = instance.bar_plot(
        x="Year", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barY = _wrapper(fig=bar, id='barY')

    FIGM = {
        "barm": barm,
        "piem": piem,
        "barD": barD,
        "barMY": barMY,
        "barY": barY
    }

    return FIGM


def EmojiFigurePlotter(DFE: dict,
                       group_name: str) -> dict:
    """
    Function to plot the plots for emojis statistics.

    Args:
        DFM(dict): Dict of dataframes containing emojis statistics.
        group_name: WhatsApp group name.

    Returns:
        FIGM(dict(Figure)): Dictionary of Plotly's figure objects.
    """
    instance = PlotlyViz(df=DFE['dfe'])
    bar = instance.bar_plot(
        x='Emojis', y='Count',
        title='Emoji count of {}'.format(group_name),
        text='Count'
    )
    pie = instance.pie_plot(
        values='Count',
        groupby='Emojis',
        title='Emoji Contribution Plot',
        color_discrete_sequence=px.colors.sequential.Plotly3
    )
    bare = _wrapper(fig=bar, id='bare')
    piee = _wrapper(fig=pie, id='piee')

    instance = PlotlyViz(df=DFE['dfeg'])
    bar = instance.bar_plot(
        x='Name', y='Count',
        title='Emoji count of {}'.format(group_name),
        text='Count'
    )
    pie = instance.pie_plot(
        values='Count',
        groupby='Name',
        title='Emoji Contribution Plot',
        color_discrete_sequence=px.colors.sequential.Plotly3
    )
    bareg = _wrapper(fig=bar, id='bareg')
    pieeg = _wrapper(fig=pie, id='pieeg')

    instance = PlotlyViz(df=DFE['dfeD'])
    bar = instance.bar_plot(
        x="Date", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    bareD = _wrapper(fig=bar, id='bareD')

    instance = PlotlyViz(df=DFE['dfeMY'])
    bar = instance.bar_plot(
        x="Month_Year", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    bareMY = _wrapper(fig=bar, id='bareMY')

    instance = PlotlyViz(df=DFE['dfeY'])
    bar = instance.bar_plot(
        x="Year", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )

    bareY = _wrapper(fig=bar, id='bareY')

    FIGE = {
        "bare": bare,
        "piee": piee,
        "bareg": bareg,
        "pieeg": pieeg,
        "bareD": bareD,
        "bareMY": bareMY,
        "bareY": bareY
    }

    return FIGE
