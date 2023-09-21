import ipywidgets as widgets

import tiktoken

MODEL = 'gtp-3.5-turbo'

def configureModel(model):
  global MODEL
  MODEL = model

def tokenize(text):
  tokens = []
  ids = []

  # To get the tokeniser corresponding to a specific model in the OpenAI API:
  encoding = tiktoken.encoding_for_model(MODEL)

  tokenized = encoding.encode(text)

  for tokenId in tokenized:
    ids.append(tokenId)
    tokens.append(encoding.decode_single_token_bytes(tokenId).decode('utf-8'))

  return (tokens, ids)

def getTokens(change):
  (tokens, ids) = tokenize(change['new'].strip())

  if tokens:
    with tokenCount:
      tokenCount.clear_output(wait=True)
      print(f"{len(tokens)} tokens")

    with tokenIds:
      tokenIds.clear_output(wait=True)
      print(f"{ids}")

    with tokenAnalysis:
      tokenAnalysis.clear_output(wait=True)
      print(f"{tokens}")
  else:
    tokenCount.clear_output()
    tokenIds.clear_output()
    tokenAnalysis.clear_output()

tokenAnalysis = widgets.Output()
tokenIds = widgets.Output()
tokenCount = widgets.Output()

tokenString = widgets.Text(
    value='',
    placeholder='Type something',
)

tokenString.observe(getTokens, names='value')

tokenAnalysisWidget = widgets.VBox([tokenString, tokenCount, tokenAnalysis, tokenIds])