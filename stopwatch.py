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
        """ returns the time to start timer """
        return time.time()

    def stop(self):
        """ returns the time to stop timer """
        return time.time()

    def min_with_sec(self, total_sec):
        """
        returns the time with min and sec.
        e.g :
            1 min 23 sec
        """

        min = total_sec / 60
        sec = total_sec % 60

        if int(min) == 0:
            return f"{sec:.0f} sec"
        else:
            return f"{min:.0f} min {sec:.0f} sec"
