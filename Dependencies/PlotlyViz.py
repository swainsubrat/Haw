"""
Contains All Plotly Visualizations
"""
from plotly.graph_objs._figure import Figure
from pandas.core.frame import DataFrame
from typing import List
import plotly.express as px
import plotly.io as pio
import pandas as pd


class PlotlyViz:
    def __init__(self,
                 df: DataFrame=None,
                 renderer: str='browser',
                 **kwargs) -> None:
        self.df = df
        pio.renderers.default = renderer

    def line_plot(self,
                  x: str,
                  y: List[str],
                  x_label: str,
                  y_label: str,
                  title: str='Line Plot',
                  range_slider: bool=False,
                  **kwargs) -> Figure:
        """
        Method for line plot
        Args:
            x (str): Column name for data of x-axis
            y (List[str]): Column names for data of y-axis
            x_label (str): Label on x-axis
            y_label (str): Label on y-axis
            title (str): Title of the plot
            range_slider (bool): Enable range slider or not

        Returns:
            fig (Figure): Figure object

        NOTE: Input kwargs should be same as plotly.express.line's
        parameters.
        Ref:
        https://plotly.com/python-api-reference/generated/plotly.express.line.html
        """
        df_long = pd.melt(self.df, id_vars=[x], value_vars=y)
        fig = px.line(df_long, x=x, y='value',
                      color='variable',
                      labels={x: x_label, y[0]: y_label},
                      title=title, **kwargs)
        if range_slider:
            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )

        return fig

    def bar_plot(self,
                 x: str,
                 y: str,
                 x_label: str=None,
                 y_label: str=None,
                 title: str='Bar Plot',
                 **kwargs) -> Figure:
        """
        Method for bar plot
        Args:
            x (str): Column name for data of x-axis
            y (str): Column name for data of y-axis
            x_label (str): Label on x-axis
            y_label (str): Label on y-axis
            title (str): Title of the plot

        Returns:
            fig (Figure): Figure object

        NOTE: Input kwargs should be same as plotly.express.bar's
        parameters.
        Ref:
        https://plotly.com/python-api-reference/generated/plotly.express.bar.html
        """
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label
        fig = px.bar(self.df, x=x, y=y,
                     labels={x: x_label, y: y_label},
                     title=title, **kwargs)
        return fig

    def corr_plot(self,
                  x_label: str,
                  y_label: str,
                  title: str='Correlation Plot',
                  **kwargs) -> Figure:
        """
        Method for correlation plot (Heatmap)
        Args:
            x_label (str): Label on x-axis
            y_label (str): Label on y-axis
            title (str): Title of the plot

        Returns:
            fig (Figure): Figure object

        NOTE: Input kwargs should be same as plotly.express.bar's
        parameters.
        Ref:
        https://plotly.com/python-api-reference/generated/plotly.express.imshow.html
        """
        corr = self.df.corr()
        fig = px.imshow(corr,
                        labels=dict(x=x_label, y=y_label),
                        x=list(self.df),
                        y=list(self.df))
        fig.update_xaxes(side="top")
        return fig

    def pie_plot(self,
                 values: str,
                 groupby: str,
                 title: str='Pie Plot',
                 **kwargs) -> Figure:
        """
        Method for line plot
        Args:
            title (str): Title of the plot

        Returns:
            fig (Figure): Figure object

        NOTE: Input kwargs should be same as plotly.express.bar's
        parameters.
        Ref:
        https://plotly.com/python-api-reference/generated/plotly.express.pie.html
        """
        fig = px.pie(self.df,
                     values=values, names=groupby,
                     title=title,
                     **kwargs)
        return fig
