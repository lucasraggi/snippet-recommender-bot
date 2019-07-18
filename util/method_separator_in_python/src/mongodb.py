import pymongo
import pymongo.errors
from pymongo import MongoClient

class MongoDb:
    def __init__(self, collection_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['java_code2vec']
        self.collection = self.db[collection_name]

    def insert(self, json):
        try:
            self.collection.insert_one(json)
            print(json)
        except:
            print('ERROR. This Object cannot be insert in collections!')

    def find(self):
        return self.collection.find()

    def find_by(self, query):
        try:
            return self.collection.find(query)
        except pymongo.errors.OperationFailure as err:
            print("ERROR in query {}".format(err))

    def delete_all_data(self):
        self.collection.delete_many({})


