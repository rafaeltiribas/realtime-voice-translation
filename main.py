# Real time speech to speech translator.
# Speech to text -> Text translation -> Text to speech.
# (Google Translate API) for [Text translation], intall using -pip install googletrans==3.1.0a0

from googletrans import Translator
import speech_recognition as sr
import pyaudio

init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    print(text)

DEST_LANGUAGE = 'pt'

# Init translator
translator = Translator()

text = 'Did you see the accident last week?'

translated_text = translator.translate(text, DEST_LANGUAGE).text

print(translated_text)
