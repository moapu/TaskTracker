# Project: Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/15/2018
# Rev: 1
# =============================
import time

from pymongo import MongoClient


class MongoDB:

    def __init__(self):
        self.__client = MongoClient('localhost', 27017)
        self.__db = self.__client.db_group2
        self.__collection = self.__db.timer

    @staticmethod
    def current_time():
        return time.strftime("%Y-%m-%d %I:%M:%S %p")

    def save(self, timer_name, duration):
        """
        save to mongo with following data:
            - timer name
            - current time
            - timer duration
        """
        entry = {'timestamp': self.current_time(), 'timer_name': timer_name, 'duration': duration}
        self.__collection.insert_one(entry)

    def get_all(self):
        cursor = self.__collection.find({})
        for document in cursor:
            print(f"{document['timestamp']} | {document['timer_name']} => {document['duration']}")

    def find_one(self, name):
        cursor = self.__collection.find({'timer_name': name})
        for document in cursor:
            print(f"{document['timestamp']} | {document['timer_name']} => {document['duration']}")

    def drop_collection(self):
        """ deletes the entire collection """
        self.__collection.drop()


if __name__ == '__main__':
    mongodb = MongoDB()
    print(mongodb.current_time())

    # get all the entry in the collection
    # mongodb.get_all()

    mongodb.find_one('dishwasher')
    # drop the collection
    # mongodb.drop_collection()
