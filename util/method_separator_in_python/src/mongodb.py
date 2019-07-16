import pymongo
import pymongo.errors
from pymongo import MongoClient

class MongoDb:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['java_code2vec']
        self.collection = self.db['methods']

    def __is_correct_to_insert(self, object):
        if object['method_name'] is not None and \
            object['code'] is not None:
            return True
        return False

    def insert(self, object):
        if self.__is_correct_to_insert(object):
            self.collection.insert_one(object)
        else:
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


