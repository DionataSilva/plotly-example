# app.py
from dash import Dash
import dash_mantine_components as dmc
from static.layout import create_layout
from callbacks.callbacks import get_callbacks
import pandas as pd

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Set layout
app.layout = create_layout(df)

get_callbacks(app, df)

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
