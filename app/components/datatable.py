from dash import dash_table

class CustomDataTable(dash_table.DataTable):
    def __init__(self, df, **kwargs):
        super().__init__(
            
            id=kwargs.get('id', 'custom-data-table'),
            data=df.to_dict('records'),
            page_size=kwargs.get('page_size', 12),
            style_table=kwargs.get('style_table', {'overflowX': 'auto'}),
        )

