# layout.py

from dash_mantine_components import Grid, Container, Title, RadioGroup, Grid, Col, Radio, Navbar, NavLink
from dash import dash_table, dcc, html
from dash_iconify import DashIconify
from components.datatable import CustomDataTable
from components.radio_group import CustomRadioGroup
from components.title import CustomTitle


def create_layout(df):
    layout = Grid([
        Col([nav_bar()], span=1),
        Col([
            CustomTitle(text='Dash de exemplo'),
            CustomRadioGroup(df),
            Container([
                dcc.Graph(figure={}, id='graph-placeholder'),
                CustomDataTable(df),
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
