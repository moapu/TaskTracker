# Project:Speech Recognition Time App
# Purpose Details: Unit Test for speech recognition
# Course: 412
# Author: Jon Ren, Raveeja Deshpande
# Date Developed: 11.16/2018
# Last Date Changed: 11/22/2018
# Rev: N/A

#test for SpeechRecognition ~STATUS~#
#---------------------------~in Progress-----------#

import unittest
import speech_recognition as sr
import speechrecognition

class UnitTestSpeechRecognition(unittest.TestCase):

    def test_recognizer(self):
        #Inputs and excepted outputs
        input_audio_filename = 'harvard.wav'
        r = sr.Recognizer()
        harvard = sr.AudioFile(input_audio_filename)
        audio = None
        with harvard as source:
            audio = r.record(source)
        
        api = speechrecognition.API.GOOGLE

        expected_output = 'the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health and zest a salt pickle taste fine with ham tacos al Pastore are my favorite a zestful food is the hot cross bun'

        # Executing function
        app = speechrecognition.SpeechApp()
        actual_output = app.recognizer(audio,api)

        #Check if input and output is the same
        self.assertEqual(expected_output, actual_output)
