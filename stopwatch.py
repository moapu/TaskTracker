# Project: Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/15/2018
# Rev: 1
# =============================
import time


class StopWatch:

    def start(self):
        return time.time()

    def stop(self):
        return time.time()

    def min_with_sec(self, total_sec):
        min = total_sec / 60
        sec = total_sec % 60
        return f"{min:.0f} min {sec:.0f} sec"

    # def stop_watch(self, command):
    #     i = 1
    #     while command != 'stop':
    #         print(i)
    #         time.sleep(1)
    #         i = i + 1
    #
    #     return i


if __name__ == '__main__':
    stopwatch = StopWatch()
    start = stopwatch.start()
    #
    time.sleep(3)
    #
    stop = stopwatch.stop()
    duration = f"{(stop - start):.0f}"
    print(duration)
    #
    # print(duration)

    # print(stopwatch.min_and_sec(65))
    # stopwatch.stop_watch()
