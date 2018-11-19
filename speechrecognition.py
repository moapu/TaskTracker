# Project:Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/03/2018
# Rev: 1
# =============================

from enum import Enum

import pyttsx3
import speech_recognition as sr

from saveToMongo import MongoDB


class API(Enum):
    """ equivalent to Java 'Enum' """
    GOOGLE = 1
    BING = 2
    SPHINX = 3


class SpeechApp:

    def __init__(self):
        """ RECOGNIZER """
        self.r = sr.Recognizer()

    def mic_input(self):
        """ return the microphone input """

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("\t*** {} ***".format("LISTENING"))
            return self.r.listen(source)

    def transcribe_from_file(self, filename):
        """ transcribe from saved audio file """

        with sr.AudioFile(filename) as source:
            print(f"\nTranscribing from {filename} ...")
            return self.r.record(source, duration=4)

    def save_audio_to_file(self, audio):
        """ saves audio to a file with '.wav' extension """

        with open('audio/mic_input_1.wav', 'wb') as f:
            f.write(audio.get_wav_data())

    def recognizer(self, audio, api):
        """ recognizes with different APIs """

        if api == API.GOOGLE:
            return self.r.recognize_google(audio)
        elif api == API.SPHINX:
            return self.r.recognize_sphinx(audio)

    def say(self, text):
        """ Text to Speech """

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 60)
        engine.say(text)
        engine.runAndWait()

    def main(self):
        try:

            # self.say("Hello World")
            # mic input
            audio = self.mic_input()
            recognized_audio = self.recognizer(audio, API.GOOGLE)
            print("\t", recognized_audio)

            import re
            result = re.findall(r'for (\w+)', recognized_audio)
            print(result)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    mongodb = MongoDB()
    s = SpeechApp()
    s.main()
