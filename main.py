#!/usr/bin/env python3

import speech_recognition as sr



# obtain path to "test.wav" in the same folder as this script
from os import path
AUDIO_FILE = "test.wav"


# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of r.recognize_google(audio)
    print(r.recognize_google(audio, key=None, language="ru_RU"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))