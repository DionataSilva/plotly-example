# layout.py

from dash_mantine_components import Container, Title, RadioGroup, Grid, Col, Radio
from dash import dash_table, dcc, html


def create_layout(df):
    layout = Container([
        Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
        RadioGroup(
            [Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
        Grid([
            Col([
                dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
            ], span=6),
            Col([
                dcc.Graph(figure={}, id='graph-placeholder')
            ], span=6),
        ]),
    ], fluid=True)

    return layout
