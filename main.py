# Real time speech to speech translator.
# Speech to text -> Text translation -> Text to speech.
# (Google Translate API) for [Text translation], intall using -pip install googletrans==3.1.0a0
# (Google Cloud - Cloud Speech to Text) for [Speech to Text], install using -pip install --upgrade google-cloud-speech

from googletrans import Translator
import speech_recognition as sr
import pyaudio
import pyttsx3

# Cloud API imports
import queue
import re
import sys
# from google.cloud import speech

DEST_LANGUAGE = 'pt'

# Init translator
translator = Translator()

# Init text-to-speech
text_speech = pyttsx3.init()

while True:
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        text = init_rec.recognize_google(audio_data)
        translated_text = translator.translate(text, DEST_LANGUAGE).text
        text_speech.say(translated_text)
        text_speech.runAndWait()
        print(translated_text)
