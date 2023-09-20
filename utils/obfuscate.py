# we'll use this to obfuscate the API key before displaying it
def obfuscateKey(key):
  buffer = 4

  if len(key) < buffer:
    buffer = 1
  elif len(key) < 8:
    buffer = 2

  middle = min(int(len(key) / 2), len(key) - buffer * 2, 10)

  return key[:buffer] + ('*' * middle) + key[(-1 * buffer):]