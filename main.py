# Real time speech to speech translator.
# Speech to text -> Text translation -> Text to speech.
# (Google Translate API) for [Text translation], intall using -pip install googletrans==3.1.0a0
# (Google Cloud - Cloud Speech to Text) for [Speech to Text], install using -pip install --upgrade google-cloud-speech

from googletrans import Translator
import speech_recognition as sr
import pyaudio

# Cloud API imports
import queue
import re
import sys
# from google.cloud import speech

'''
init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    print(text)
'''

DEST_LANGUAGE = 'pt'

# Init translator
translator = Translator()

text = 'Did you see the accident last week?'

translated_text = translator.translate(text, DEST_LANGUAGE).text

print(translated_text)
