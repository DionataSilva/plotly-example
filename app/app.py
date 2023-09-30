# app.py
from dash import Dash
import dash_mantine_components as dmc
from static.layout import create_layout
from callbacks.callbacks import get_callbacks
import pandas as pd
import gdown
import os


# url = "https://drive.google.com/uc?id=1-9DD5AOL40nmB63eJpZZzNbLnYJw1Us9"
# output = "temp/Mental disorder symptoms.xlsx"

# if not os.path.exists("temp"):
#     os.makedirs("temp")

# gdown.download(url, output, quiet=False)

# df = pd.read_excel(output)

# df = df.rename(columns={'ag+1:629e':'age'})
# df = df.rename(columns={'having.trouble.in.sleeping':'trouble.sleeping'})
# df = df.rename(columns={'having.trouble.with.work':'trouble.with.work'})
# df = df.rename(columns={'having.nightmares':'nightmares'})

# df.set_index(['age'])


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
