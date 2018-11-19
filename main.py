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


def start_timer(recognized_audio):
    """ starts the timer """
    if "start a timer" in recognized_audio or "start timer" in recognized_audio:
        return stopwatch.start()


def stop_timer(recognized_audio):
    """  stops the timer """
    if "stop timer" in recognized_audio:
        return stopwatch.stop()


def calc_total_sec(start, stop):
    """ calculate the sec for chore """
    str_val = "{:.0f}".format((stop - start))
    return int(str_val)


def prompt(title):
    print("\t*** {} ***".format(title).upper())


def title(name):
    print(f"\t+{(len(name)+2) * '-'}+")
    print(f"\t| {name} |")
    print(f"\t+{(len(name)+2) * '-'}+\n")
    prompt("wait for voice activation")


def print_duration():
    prompt = "DURATION"
    t = total_time
    length = len(prompt) + len(t) + 2
    print("\t", length * '=')
    print(f"\t {prompt}: {t}")
    print("\t", length * '=')
    print()


if __name__ == '__main__':
    """ MAIN FUNC """

    # === TITLE ===
    title("SPEECH APP")

    # === INSTANTIATION ===
    speech = SpeechApp()
    mongodb = MongoDB()
    stopwatch = StopWatch()

    # === ITERATIONS ===
    q_iterations = ["what", "what's", "what is"]
    x_iterations = ["close", "exit", "turn off"]

    # === TIMER ===
    start_time = ''
    stop_time = ''
    total_sec = ''

    # === LAST COMMAND ===
    last_command = ''

    # === START ===
    speech.say("What chore do you want to time? ")
    while True:
        try:
            audio = speech.mic_input()
            recognized_audio = speech.recognizer(audio, API.GOOGLE)
            print("\nYou said: '{}'\n".format(recognized_audio))
        except Exception:
            continue

        # last command
        if last_command == recognized_audio:
            prompt("cannot do that")
            continue

        # save last command
        last_command = recognized_audio

        # start timer
        temp = start_timer(recognized_audio)
        if isinstance(temp, float):
            start_time = temp
            prompt("timer started")
            continue

        # stop timer
        temp = stop_timer(recognized_audio)
        if isinstance(temp, float):
            stop_time = temp
            total_sec = calc_total_sec(start_time, stop_time)
            total_time = stopwatch.min_with_sec(total_sec)

            # reset to empty again
            start_time = ''
            stop_time = ''
            print_duration()
            continue

        # question_iteration(q_iterations, recognized_audio)
        exit_iteration(x_iterations, recognized_audio)
