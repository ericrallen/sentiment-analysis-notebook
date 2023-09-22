import ipywidgets as widgets

# import the VADER sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# instantiate the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def convertSentimentToLabel(sentiment):
  sentimentScore = sentiment['compound']

  if sentimentScore >= 0.75:
    return('very positive')
  elif sentimentScore >= 0.4:
    return('positive')
  elif sentimentScore >= 0.1:
    return('leaning positive')
  elif sentimentScore <= -0.1 and sentimentScore > -0.4:
    return('leaning negative')
  elif sentimentScore <= -0.4 and sentimentScore > -0.75:
    return('negative')
  elif sentimentScore <= -0.75:
    return('very negative')
  else:
    return('neutral')


def analyzeSentiment(text):
  if not text:
    return('')

  return analyzer.polarity_scores(text)

def getSentiment(change):
  # Get the sentiment
  sentiment = analyzeSentiment(change['new'].strip())

  if sentiment:
    with analysis:
      analysis.clear_output(wait=True)
      print(convertSentimentToLabel(sentiment))
  else:
    analysis.clear_output()

analysis = widgets.Output(layout=widgets.Layout(margin_left='10px'))

demoString = widgets.Text(
    value='',
    placeholder='Type something',
)

demoString.observe(getSentiment, names='value')

simpleAnalysisWidget = widgets.Box([demoString, analysis], layout=widgets.Layout(display='flex', flex_direction='row', align_items='center', width='100%'))