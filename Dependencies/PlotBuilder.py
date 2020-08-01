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


def FiguresPlotter(DF: dict, group_name: str) -> dict:
    FIG = {}
    instance = PlotlyViz(df=DF['dfm'])
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

    instance = PlotlyViz(df=DF['dfmD'])
    bar = instance.bar_plot(
        x="Date", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barD = _wrapper(fig=bar, id='barD')

    instance = PlotlyViz(df=DF['dfmMY'])
    bar = instance.bar_plot(
        x="Month_Year", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barMY = _wrapper(fig=bar, id='barMY')

    instance = PlotlyViz(df=DF['dfmY'])
    bar = instance.bar_plot(
        x="Year", y="Count",
        title='Message count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    barY = _wrapper(fig=bar, id='barY')

    instance = PlotlyViz(df=DF['dfe'])
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

    instance = PlotlyViz(df=DF['dfeg'])
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

    instance = PlotlyViz(df=DF['dfeD'])
    bar = instance.bar_plot(
        x="Date", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    bareD = _wrapper(fig=bar, id='bareD')

    instance = PlotlyViz(df=DF['dfeMY'])
    bar = instance.bar_plot(
        x="Month_Year", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )
    bareMY = _wrapper(fig=bar, id='bareMY')

    instance = PlotlyViz(df=DF['dfeY'])
    bar = instance.bar_plot(
        x="Year", y="Count",
        title='Emoji count of {} group, (per day)'.format(group_name),
        text='Count'
    )

    bareY = _wrapper(fig=bar, id='bareY')

    FIG['barm'], FIG['barD'], FIG['barMY'], FIG['barY'] =\
        barm, barD, barMY, barY
    FIG['piem'], FIG['piee'], FIG['pieeg'] = piem, piee, pieeg
    FIG['bare'], FIG['bareg'], FIG['bareD'], FIG['bareMY'], FIG['bareY'] =\
        bare, bareg, bareD, bareMY, bareY

    return FIG
