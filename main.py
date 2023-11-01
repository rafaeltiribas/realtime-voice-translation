# Real time speech to speech translator.
# Speech to text -> Text translation -> Text to speech.

# (Google Translate API)  [Text translation]

from googletrans import Translator

# Init translator
translator = Translator()

text1 = 'Did you see the accident last week?'
#print(translator.detect(text1))