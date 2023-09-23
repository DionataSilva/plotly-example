# callbacks.py

from dash import callback, Output, Input
import plotly.express as px

def get_callbacks(app):
    @app.callback(
        Output(component_id='graph-placeholder', component_property='figure'),
        Input(component_id='my-dmc-radio-item', component_property='value')
    )
    def update_graph(col_chosen, df):  # Adicione df como um argumento
        fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
        return fig

    @app.callback([Output("figure2", "figure")],
                  [Input("child2", "value")])
    def callback2(figure):
        return
