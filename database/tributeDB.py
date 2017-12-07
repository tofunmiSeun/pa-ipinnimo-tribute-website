import pymongo
from pymongo import MongoClient
from models.tribute import Tribute
from utils.constants import Constants
import time


class TributeDB:
    COLLECTION_NAME = 'tributes'

    @staticmethod
    def add_new_tribute(tribute_object):
        try:

            now = int(round(time.time() * 1000))

            obj = {
                'name': tribute_object['name'],
                'content': tribute_object['content'],
                'dateAdded': now
            }

            client = MongoClient(Constants.DB_CONNECTION_URL)
            document = client[Constants.DB_NAME][TributeDB.COLLECTION_NAME]

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to add new tribute')
            raise Exception('Could not add new tribute to DB')

    @staticmethod
    def get_all_tributes():
        try:
            client = MongoClient(Constants.DB_CONNECTION_URL)
            document = client[Constants.DB_NAME][TributeDB.COLLECTION_NAME]

            tributes = document.find({}).sort([("dateAdded", pymongo.DESCENDING)])
            all_tributes = []

            for t in tributes:
                tribute_obj = Tribute(t['name'], t['content'], t['dateAdded'])
                all_tributes.append(tribute_obj)

            client.close()
            return all_tributes

        except Exception as e:
            print('unable to get tributes')
            raise Exception('Could not get tributes from DB')
