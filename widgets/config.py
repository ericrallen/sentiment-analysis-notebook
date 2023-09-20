import os

import ipywidgets as widgets

apiKeyInput = widgets.Text(
  value='',
  placeholder='Enter your OpenAI API key',
  description='OpenAI API Key',
)

apiKeyUpdateButton = widgets.Button(
  description='Update',
  disabled=False,
  button_style='danger',
)

modelDropdown = widgets.Dropdown(
  options=[('GPT-3.5 Turbo', "gpt-3.5-turbo"), ('GPT-4', 'gpt-4')],
  value='gpt-3.5-turbo',
  description='Model',
)