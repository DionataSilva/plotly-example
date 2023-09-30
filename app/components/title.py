import dash_mantine_components as dmc

class CustomTitle(dmc.Title):
    def __init__(self, **kwargs):
        super().__init__(
            id=kwargs.get('id', 'custom-text'),
            color=kwargs.get('color', 'blue'),
            size=kwargs.get('size', 'h3'),
            children=kwargs.get('text', 'My First App with Data, Graph, and Controls'),
        )