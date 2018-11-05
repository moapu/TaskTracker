# Project:Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/03/2018
# Rev: 1

import speech_recognition as sr


# get audio from the microphone
r = sr.Recognizer()  # RECOGNIZE

with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
try:
    if r.recognize_google(audio) == "test":
        print("You said " + r.recognize_google(audio))
    elif r.recognize_google(audio) != "test":
        print(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


