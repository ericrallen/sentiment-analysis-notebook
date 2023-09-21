import ipywidgets as widgets

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nrclex import NRCLex

import openai


analyzer = SentimentIntensityAnalyzer()

ADVANCED_SYSTEM_PROMPT = """
You are VibeCheck, an advanced AI system for detecting the sentiment conveyed in user-generated text.

The user will provide you with a prompt, and you will analyze it following these steps:

1. Analyze the prompt for relevant emotion, tone, affinity, sarcasm, irony, etc.
2. Analyze the likely emotional state of the author based on those findings
3. Summarize the emotional state and sentiment of the prompt based on your findings using 5 or less names for emotions using lowercase letters and separating each emotional state with a comma

Only return the output from the final step to the user.
"""

OPEN_AI_MODEL = 'gpt-3.5-turbo'
TEMPERATURE = 0.2

def configureOpenAi(key, model, temp):
  global OPEN_AI_MODEL
  global TEMPERATURE

  openai.api_key = key
  OPEN_AI_MODEL = model
  TEMPERATURE = temp


def advancedChatGptSentiment(prompt):
    messages = [{ "role": "system", "content": ADVANCED_SYSTEM_PROMPT }]

    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=OPEN_AI_MODEL,
        messages=messages,
        temperature=0.15,
    )

    return response.choices[0].message["content"]


# analyze the sentiment of a string of text
def analyzeBasicSentiment(text):
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


def getNRCEmotion(text):
  emotion = NRCLex(text)

  return emotion.top_emotions


def getAdvancedSentiment(event):
  text = advancedDemoString.value.strip()

  # Get the sentiment
  sentiment = analyzeBasicSentiment(text)
  emotions = getNRCEmotion(text)
  openAiSentiment = advancedChatGptSentiment(text)

  if sentiment:
    with basicAnalysis:
      basicAnalysis.clear_output(wait=True)
      print(f"VADER: {sentiment}")
  else:
    basicAnalysis.clear_output()

  if emotions:
    with nrcLexAnalysis:
      nrcLexAnalysis.clear_output(wait=True)
      print(f"NRC: {emotions}")
  else:
    nrcLexAnalysis.clear_output()

  if openAiSentiment:
    with advancedAnalysis:
      advancedAnalysis.clear_output(wait=True)
      print(f"{OPEN_AI_MODEL}: {openAiSentiment}")
  else:
    advancedAnalysis.clear_output()


basicAnalysis = widgets.Output()
nrcLexAnalysis = widgets.Output()
advancedAnalysis = widgets.Output()

advancedAnalysisButton = widgets.Button(
  description='Analyze',
  button_style='primary',
)

advancedDemoString = widgets.Text(
    value='',
    placeholder='Type something',
)

advancedAnalysisButton.on_click(getAdvancedSentiment)

advancedAnalysisInput = widgets.HBox([advancedDemoString, advancedAnalysisButton])
advancedAnalysisOutput = widgets.VBox([basicAnalysis, nrcLexAnalysis, advancedAnalysis])

advancedAnalysisWidget = widgets.VBox([advancedAnalysisInput, advancedAnalysisOutput])