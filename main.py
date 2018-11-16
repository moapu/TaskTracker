# Project: Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/03/2018
# Rev: 1
# =============================
import sys

from saveToMongo import MongoDB
from speechrecognition import SpeechApp, API
from stopwatch import StopWatch


def exit_iteration(iteration, recognized_audio):
    """ iterations for exiting program. program closes
    if the words in 'x_iterations' are recognized """

    for i in iteration:
        if i in recognized_audio:
            sys.exit()


def question_iteration(iteration, recognized_audio):
    """ iterations for retrieving timer. program retrieves
    timer for mongodb if the words in 'q_iterations' are
    recognized """

    for i in q_iterations:
        if i in recognized_audio:
            print("true")
            break


if __name__ == '__main__':
    """ MAIN FUNC """

    # === INSTANTIATION ===
    speech = SpeechApp()
    mongodb = MongoDB()
    stopwatch = StopWatch()

    # === ITERATIONS ===
    q_iterations = ["what", "what's", "what is"]
    x_iterations = ["close", "exit", "turn off"]

    # === START ===
    speech.say("What chore do you want to time? ")
    while True:
        # audio input
        audio = speech.mic_input()
        recognized_audio = speech.recognizer(audio, API.GOOGLE)
        print("\t", recognized_audio)

        question_iteration(q_iterations, recognized_audio)
        exit_iteration(x_iterations, recognized_audio)

        # start timer
        start_time = stopwatch.start()
        speech.say("Timer started")
        print("\nTimer started")
