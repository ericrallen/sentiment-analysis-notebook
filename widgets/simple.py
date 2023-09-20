import ipywidgets as widgets

# import the VADER sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# instantiate the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# analyze the sentiment of a string of text
def analyzeSentiment(text):
  if not text:
    return('')

  # use VADER to get the +/- sentiment of the string
  sentiment = analyzer.polarity_scores(text)

  # map the sentiment to a human readable label
  if sentiment['compound'] >= 0.75:
    return('Very Positive')
  elif sentiment['compound'] >= 0.4:
    return('Positive')
  elif sentiment['compound'] >= 0.1:
    return('Leaning Positive')
  elif sentiment['compound'] <= -0.1 and sentiment['compound'] > -0.4:
    return('Leaning Negative')
  elif sentiment['compound'] <= -0.4 and sentiment['compound'] > -0.75:
    return('Negative')
  elif sentiment['compound'] <= -0.75:
    return('Very Negative')
  else:
    return('Neutral')

def getSentiment(change):
  # Get the sentiment
  sentiment = analyzeSentiment(change['new'].strip())

  with analysis:
    if sentiment:
      analysis.clear_output(wait=True)
      print(sentiment)
    else:
      analysis.clear_output()

analysis = widgets.Output(layout=widgets.Layout(margin_left='10px'))

demoString = widgets.Text(
    value='',
    placeholder='Type something',
)

demoString.observe(getSentiment, names='value')

simpleAnalysisWidget = widgets.Box([demoString, analysis], layout=widgets.Layout(display='flex', flex_direction='row', align_items='center', width='100%'))