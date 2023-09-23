import dash_table
import pandas as pd


class DataTable(dash_table.DataTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data = df.to_dict('records')
        self.page_size = 12
        self.style_table = {'overflowX': 'auto'}

