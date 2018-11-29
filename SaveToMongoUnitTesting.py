# Project:Speech Recognition Time App
# Purpose Details: Unit Test for MongoDB
# Course: 412
# Author: Jon Ren, Raveeja Deshpande
# Date Developed: 11/28/2018
# Last Date Changed: 11/28/2018
# Rev: N/A

import unittest
import datetime
from saveToMongo import MongoDB


class UnitTestDB(unittest.TestCase):
    """Unit Testing class saveToMongo"""

    def test_Current_Time(self):
        """ Test current time method"""
        my_time = datetime.datetime("%Y-%m-%d %I:%M:%S %p")
        response_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
        self.assertEqual(response_time, my_time)

    #To be continue
    def test_Save(self):
        """ Testing The following Save
            - timer name
            - current time
            - timer duration
        """
        self.assertTrue(True)
    #To Be continue
    def find_all(self):
        """ Testing finding entry from MongoDB include timestamp
            for document in cursor: print(f"{document['timestamp']
            }|{document['timer_name']} => {document['duration']}")
        """
        self.assertTrue(True)
    #To Be continue
    def find_one(self):
        """Testing one entry for Mongo"""
        self.assertTrue(True)

    def test_Drop(self):
        """Testing to see if the entire is drop, if True then its 
	   drop
	"""
        self.assertTrue(MongoDB.drop_collection, True)

