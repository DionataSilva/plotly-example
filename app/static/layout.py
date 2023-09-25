# layout.py

from dash_mantine_components import Grid, Container, Title, RadioGroup, Grid, Col, Radio, Navbar, NavLink
from dash import dash_table, dcc, html
from dash_iconify import DashIconify


def create_layout(df):
    layout = Grid([
        Col([nav_bar()], span=1),
        Col([
            Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
            RadioGroup(
                [Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']],
                id='my-dmc-radio-item',
                value='lifeExp',
                size="sm"
            ),
            Container([
                dcc.Graph(figure={}, id='graph-placeholder'),
                dash_table.DataTable(
                        id='data-table', 
                        data=df.to_dict("records"),
                        page_size=12, 
                        style_table={'overflowX': 'auto'}
                    ),
            ], fluid=True),
        ], span=10),

    ],  gutter="xl", grow=True)

    return layout


def nav_bar():
    return Navbar(
                    p="md",
                    width={"base": 300},
                    height="100vh",
                    style={'backgroundColor':'whitesmoke'},
                    children=[
                        NavLink(
                            label="Resume Builder",
                            href='/resumeBuilder',
                            children=[
                                DashIconify(icon='fluent-mdl2:issue-tracking'),
                                "Resume Builder",
                            ]
                        ),
                    ],
                )
