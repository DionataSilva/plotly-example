# callbacks.py

from dash import callback, Output, Input
import plotly.express as px

def get_callbacks(app, df):
    @app.callback(
        Output(component_id='graph-placeholder', component_property='figure'),
        Input(component_id='custom-dmc-radio-item', component_property='value')
    )
    def update_graph(col_chosen):
        fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
        # print(col_chosen)
        # print(df)
        # print(fig)
        return fig

    @app.callback(
        Output(component_id='custom-data-table', component_property='data'),
        Input(component_id='custom-dmc-radio-item', component_property='value')
    )
    def update_data_table(col_chosen):  
        # print(df.to_dict('records'))

        return df.to_dict('records')
