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
    """
    iterations for exiting program. program closes
    if the words in 'x_iterations' are recognized
    """

    for i in iteration:
        if i in recognized_audio:
            sys.exit()


def question_iteration(iteration, recognized_audio):
    """
    iterations for retrieving timer. program retrieves
    timer for mongodb if the words in 'q_iterations' are
    recognized
    """

    import re
    timer_name = re.findall(r'for (\w+)', recognized_audio)

    for i in q_iterations:
        if i in recognized_audio:
            break

    return mongodb.find_one(timer_name[0])


def start_timer(recognized_audio):
    """
    returns the current time if audio is equal to the following:
        - start a timer
        - start time
    """

    if "start a timer" in recognized_audio or "start timer" in recognized_audio:
        return stopwatch.start()


def return_timer_name(recognized_audio):
    """
    uses regex to validate the timer name.
    if no name, it prompts
    else, returns the name.
    """

    import re
    timer_name = re.findall(r'for (\w+)', recognized_audio)

    if not timer_name:
        prompt("need a name")
        return None
    else:
        return timer_name[0]


def stop_timer(recognized_audio):
    """
    returns the current time if audio is equal to the following:
        - stop time
    """
    if "stop timer" in recognized_audio:
        return stopwatch.stop()


def calc_total_sec(start, stop):
    """ returns the total sec in Integer form """
    return stop - start


def prompt(title):
    """
    shows whats happening from the programmers POV.
    e.g:
        *** LISTENING ***
    """
    print("\t*** {} ***".format(title).upper())


def title(name):
    """
    displays the app name on the top.
    e.g:
        +------------+
        | SPEECH APP |
        +------------+
    """
    print(f"\t+{(len(name)+2) * '-'}+")
    print(f"\t| {name} |")
    print(f"\t+{(len(name)+2) * '-'}+\n")
    prompt("wait for voice activation")


def print_duration():
    """
    prints the total time of the chore in nice format.
    e.g:
         ================
         DURATION: 15 sec
         ================
    """
    prompt = "DURATION"
    t = total_time
    length = len(prompt) + len(t) + 2
    print("\t", length * '=')
    print(f"\t {prompt}: {t}")
    print("\t", length * '=')
    print()


if __name__ == '__main__':

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
    total_time = ''
    timer_name = ''

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

        exit_iteration(x_iterations, recognized_audio)
        question_iteration(q_iterations, recognized_audio)

        # last command
        if last_command == recognized_audio:
            prompt("cannot do that")
            continue

        # save last command
        last_command = recognized_audio

        # stop timer
        temp = stop_timer(recognized_audio)
        if isinstance(temp, float):
            stop_time = temp
            total_sec = calc_total_sec(start_time, stop_time)
            total_time = stopwatch.min_with_sec(int(total_sec))

            # print duration
            print_duration()

            # save the time
            mongodb.save(timer_name, total_time)
            prompt("timer saved")

            # reset to empty again
            start_time = ''
            stop_time = ''
            total_time = ''
            timer_name = ''
            continue

        # check if the name was given
        if timer_name == '':
            temp = return_timer_name(recognized_audio)
            if temp is None:
                continue
            else:
                timer_name = temp

        # start timer
        temp = start_timer(recognized_audio)
        if isinstance(temp, float):
            start_time = temp
            prompt("timer started")
            continue
