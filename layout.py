import dash_html_components as html
import dash_bootstrap_components as dbc

from typing import Any, List


class BootstrapComponents:
    """
    Abstract class for different bootstrap components
    """
    def __init__(self):
        pass

    def add_columns(self,
                    n_cols: int=2,
                    elements: List[Any]=None,
                    no_gutters: bool=False) -> dbc.Row:
        """
        Display in columns

        Args:
            n_cols(int): number of columns.
            elements(List[Any]): List of element of any type supported
            by plotly.
            no_gutters(bool): whether to pad or not.

        Returns:
            row(dbc.Row): row of requested format
        """
        cols = []
        for i in range(n_cols):
            cols.append(dbc.Col(html.Div(elements[i])))
        row = dbc.Row(cols, no_gutters=no_gutters)

        return row
