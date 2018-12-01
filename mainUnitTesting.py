# Project:Speech Recognition Time App
# Purpose Details: Unit Test for main
#
# Author Raveeja, Jon
# Date Developed: 11/28/2018
# Last Date Changed: 11/28/2018
# Rev: n/a

#test for main

import unittest
import main
import time
from saveToMongo import MongoDB
from speechrecognition import SpeechApp, API


class UnitTestMain(unittest.TestCase):

    def test_exit_iteration(self):

       #Input and expected outputs
       iteration = [0]
       recognized_audio = [0,1,2]
       expected_exit_code = None

       #Executing funciton
       with self.assertRaises(SystemExit) as cm:
           main.exit_iteration(iteration,recognized_audio)

       #Check if input and output is same
       self.assertEqual(cm.exception.code, expected_exit_code)


    def test_query_timer(self):
        """
        This tests recognized three recognized audio
        1. Doesn't contain what's -> output is None
        2. Contains what's but not for * -> output is None
        3. Contains what's and name -> output is 'timer_value'
        """

        class MockMongoDb:
            def find_one(self, timer_name):
                return 'timer_value'

        main.mongodb = MockMongoDb()
        
        # Test 1
        # Inputs and expected output
        recognized_audio = ''
        expected_output = None

        # Execute function 
        actual_output = main.query_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)

        # Test 2
        # Inputs and expected output
        recognized_audio = 'what is'
        expected_output = None

        # Execute function 
        actual_output = main.query_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)

        # Test 3
        # Inputs and expected output
        recognized_audio = 'what is for dinner'
        expected_output = 'timer_value'

        # Execute function 
        actual_output = main.query_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)

    def test_start_timer(self):
        """
        This tests recognized three recognized audio
        1. Doesn't contain what's -> output is None
        2. Contains what's but not for * -> output is None
        3. Contains what's and name -> output is 'timer_value'
        """

        # Test 1
        # Inputs and expected output
        recognized_audio = ''
        expected_output = None

        # Execute function 
        actual_output = main.start_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)

        # Test 2
        # Inputs and expected output
        recognized_audio = 'start a timer'
        expected_output = None

        # Execute function 
        actual_output = main.start_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)

        # Test 3
        # Inputs and expected output
        recognized_audio = 'start a timer for dinner'
        expected_output = 'dinner'

        # Execute function 
        actual_output = main.start_timer(recognized_audio)

        # Check if input and output is same
        self.assertEqual(actual_output, expected_output)
    def test_stop_timer(self):
       """
       this test 2 inputs for recognized audio
       1. input doesnt contain stop timer -> output is none
       2. input contains stop timer -> output is current time
       
       Checking if this is the current time by calculating the 
       difference. It should be less than 5 seconds (assuming the 
       test runs less than 5 seconds) 
       """

       #Test 1
       #Inputs and expected output
       recognized_audio = ' '
       expected_output = None

       #Excute function
       actual_output = main.stop_timer(recognized_audio)

       #Check if input and output are same
       self.assertEqual(actual_output, expected_output)

       #Test 2
       #Inputs and expected output
       recognized_audio = 'stop timer '
       expected_output = time.time()

       #Excute function
       actual_output = main.stop_timer(recognized_audio)

       #Check if input and output within 5 seconds
       self.assertLessEqual(actual_output - expected_output, 5)

    def test_calc_total_sec(self):
       """
       This test will start at 0 and it will stop at 10 
       

       """
       start = 0
       stop = 10
       #Inputs and expeced output
       expected_output = 10
       #Excute function
       actual_output = main.calc_total_sec(stop, start)
       #Check if input and output 
       self.assertLessEqual(actual_output, expected_output)

    def test_min_with_sec(self):
       """	
       Test will implement the total sec excuted
       """
       total_sec = 63
       #Inputs and expected output
       expected_output = "1 min 3 sec"
       #Excute function
       actual_output = main.min_with_sec(total_sec)
       #Check if input and output 
       self.assertEqual(actual_output, expected_output)

    def test_prompt(self):
      """
      Tests the prompt method. It doesn't check for expected outputs
      because the function doesn't return anything. It only checks that
      the method runs without errors.
      """
      #Inputs
      title = 'Hello'
      #Excute function
      main.prompt(title)
      #No output to check here

    def test_title(self):
      """
      Tests the title method. It doesn't check for expected outputs
      because the function doesn't anything.It only checks that 
      the method runs without errors 
      """
      #Inputs
      name = 'Speech recognition app'
      #Excute function
      main.title(name)
      #No output to check here

    def test_duration(self):
      """
      Tests the duration method.It doesn't check for expected outputs 
      because the funciton doesn't return anything. It only checks that 
      the method runs without errors. 
      """
      main.total_time = ''
      #Execute function
      main.print_duration()





