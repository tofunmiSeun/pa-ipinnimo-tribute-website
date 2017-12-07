from pymongo import MongoClient
from bson.objectid import ObjectId
from models.tribute import Tribute
from utils.constants import Constants


class TributeDB:
    COLLECTION_NAME = 'tributes'

    @staticmethod
    def add_new_tribute(tribute_object):
        try:
            obj = {
                'name': tribute_object['name'],
                'content': tribute_object['content'],
                'dateAdded': tribute_object['dateAdded']
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

            tributes = document.find({})
            all_tributes = []

            for t in tributes:
                tribute_obj = {
                    'name': t['name'],
                    'content': t['content'],
                    'dateAdded': t['dateAdded']
                }

                all_tributes.append(t)

            client.close()
            return all_tributes

        except Exception as e:
            print('unable to get tributes')
            raise Exception('Could not get tributes from DB')
