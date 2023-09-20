import ipywidgets as widgets

sampleSizeSlider = widgets.IntSlider(
  value=1,
  min=1,
  max=100,
  step=1,
  description='Sample Size:',
  continuous_update=False,
  orientation='horizontal',
  readout=True,
  readout_format='d'
)

sampleSizeWarningLabel = widgets.Label(
  value='Warning: Increasing the sample size will result in more tokens being sent to the OpenAI API.'
)