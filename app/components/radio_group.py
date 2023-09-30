import dash_mantine_components as dmc
import pandas as pd


class CustomRadioGroup(dmc.RadioGroup):
    def __init__(self, df, **kwargs):
        # Filtra as colunas do DataFrame que contêm valores numéricos
        numeric_columns = [
            col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])
        ]

        defaultOption = numeric_columns[0] if numeric_columns else None

        super().__init__(
            id=kwargs.get("id", "custom-dmc-radio-item"),
            value=kwargs.get("defaultOption", defaultOption),
            size=kwargs.get("size", "sm"),
            children=kwargs.get(
                "options",
                [dmc.Radio(option, value=option) for option in numeric_columns],
            ),
        )
