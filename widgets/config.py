import ipywidgets as widgets

openAiHeader = widgets.Label(
    "OpenAI API", style=dict(font_size="1.2rem", font_weight="bold")
)
lakeraHeader = widgets.Label(
    "Lakera Guard API", style=dict(font_size="1.2rem", font_weight="bold")
)
hackerNewsHeader = widgets.Label(
    "Hacker News API", style=dict(font_size="1.2rem", font_weight="bold")
)

apiKeyInput = widgets.Text(
    value="",
    placeholder="Enter your OpenAI API key",
    description="API Key",
)

apiKeyUpdateButton = widgets.Button(
    description="Update OpenAI Key",
    disabled=False,
    button_style="primary" if not apiKeyInput.value else "danger",
)

lakeraKeyInput = widgets.Text(
    value="",
    placeholder="Enter your Lakera Guard API key",
    description="Lakera Key",
)

lakeraKeyUpdateButton = widgets.Button(
    description="Update Lakera Key",
    disabled=False,
    button_style="primary" if not lakeraKeyInput.value else "danger",
)

modelDropdown = widgets.Dropdown(
    options=["gpt-3.5-turbo", "gpt-4"],
    value="gpt-3.5-turbo",
    description="Model",
)

temperatureSlider = widgets.FloatSlider(
    value=0,
    min=0,
    max=2,
    step=0.01,
    description="Temp",
    continuous_update=False,
    orientation="horizontal",
    readout=True,
    readout_format=".2f",
)

sampleSizeSlider = widgets.IntSlider(
    value=1,
    min=1,
    max=100,
    step=1,
    description="Samples",
    continuous_update=False,
    orientation="horizontal",
    readout=True,
    readout_format="d",
)

sampleSizeWarningLabelPrefix = widgets.Label(
    value="Warning:", style=dict(font_weight="bold")
)

sampleSizeWarningLabelContent = widgets.Label(
    value="Increasing sample size will result in higher costs."
)

sampleSizeWarningLabel = widgets.HBox(
    [sampleSizeWarningLabelPrefix, sampleSizeWarningLabelContent]
)
