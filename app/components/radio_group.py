import dash_mantine_components as dmc

class RadioGroup(dmc.RadioGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.options = [
            dmc.Radio(i, value=i) for i in ['pop', 'lifeExp', 'gdpPercap']
        ]
        self.value = 'lifeExp'
        self.size = 'sm'
