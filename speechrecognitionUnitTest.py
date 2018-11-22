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
import os.path

class UnitTestSpeechRecognition(unittest.TestCase):

    def test_transcribe_and_recognizer(self):
        """
        This function will take a prerecord input from a file and check
        it with the expected transcription.

        Since we are reading an audio file to transcribe, it makes sense
        to test both the functions in the same test case.
        """

        #Inputs and excepted outputs
        input_audio_filename = 'harvard.wav'
        api = speechrecognition.API.GOOGLE

        expected_output = 'the stale smell of old beer lingers'

        # Executing function
        app = speechrecognition.SpeechApp()
        audio = app.transcribe_from_file(input_audio_filename)
        actual_output = app.recognizer(audio,api)

        #Check if input and output is the same
        self.assertEqual(expected_output, actual_output)

    def test_save_audio_to_file(self):
        """
        This funciton will read audio from a file. It will check if
        the output file exists.
        """

        #Inputs and expected outputs
        input_audio_filename = 'harvard.wav'
        output_audio_filename = 'audio/mic_input_1.wav'

        #Execute function
        app = speechrecognition.SpeechApp()
        audio = app.transcribe_from_file(input_audio_filename)
        app.save_audio_to_file(audio)

        #Check if the file exists
        self.assertTrue(os.path.isfile(output_audio_filename))