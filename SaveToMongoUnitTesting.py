# Project:Speech Recognition Time App
# Purpose Details: Unit Test for MongoDB
# Course: 412
# Author: Jon Ren, Raveeja Deshpande
# Date Developed: 11/28/2018
# Last Date Changed: 11/28/2018
# Rev: N/A

import unittest
import saveToMongo
import time
from saveToMongo import MongoDB 

class UnitTestsaveToMongo(unittest.TestCase):

    def test_init(self):
       '''
       This will initialize MongoDB class and verify 
       that it is not None
       '''
       
       #Execute
       mongo_db = saveToMongo.MongoDB()

       #Verify mongo_db is not None
       self.assertIsNotNone(mongo_db)

    def test_current_time(self):
       '''
       This tests if the current time is the same
       string representation
       '''
       #Inputs and expected output
       expected_output = time.strftime('%Y-%m-%d %I:%M:%S %p')
       #Execute function
       actual_output = saveToMongo.MongoDB().current_time()
       #Check if input and output is same
       self.assertEqual(actual_output, expected_output)

       
    def test_save(self):
       '''
       This tests if the duration is saved against the timer name.
       '''
       timer_name = 'timer_name'
       duration = 5

       class MockCollection():
          def __init__(self):
              self.data = []

          def insert_one(self,value):
               self.data.append(value)

       #Execute function
       mongo_db = saveToMongo.MongoDB()
       mongo_db._MongoDB__collection = MockCollection()
       mongo_db.save(timer_name, duration)

       #Assert collection is not empty
       self.assertGreater(len(mongo_db._MongoDB__collection.data),0)

    def test_drop_collection(self):
       '''
       This tests if the collection is empty. It defins a 
       MockCollection that starts.with a filled list. Calling
       drop() on it will empty the collection. Again, here we are 
       not testing mongodb. We just need to verify if the drop()
       method is called on the collection
       '''
       #Expected function
       expected_collection_count = 0

       class MockCollection():
          def __init__(self):
              self.data = [1, 2, 3]

          def drop(self):
           	   self.data.clear()

       #Execute function
       mongo_db = saveToMongo.MongoDB()
       mongo_db._MongoDB__collection = MockCollection()
       mongo_db.drop_collection()

       #Assert collection is not empty
       
self.assertEqual(len(mongo_db._MongoDB__collection.data),expected_collection_count)
