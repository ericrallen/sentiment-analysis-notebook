import ipywidgets as widgets

apiKeyInput = widgets.Text(
  value='',
  placeholder='Enter your OpenAI API key',
  description='OpenAI API Key',
)

apiKeyUpdateButton = widgets.Button(
  description='Update',
  disabled=False,
  button_style='primary' if not apiKeyInput.value else 'danger',
)

modelDropdown = widgets.Dropdown(
  options=['gpt-3.5-turbo', 'gpt-4'],
  value='gpt-3.5-turbo',
  description='Model',
)