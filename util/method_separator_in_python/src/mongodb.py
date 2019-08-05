import pymongo
import pymongo.errors
from pymongo import MongoClient
from bson.son import SON
import pprint


class MongoDb:
    def __init__(self, collection_name):
        self.client = MongoClient('localhost', 27017)
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

    def rank_by_occurrence(self):
        pipeline = [
            {'$unwind': '$method_name'},
            {'$group': {'_id': '$method_name', 'count': {'$sum': 1}}},
            {'$sort': SON([("count", -1), ("_id", -1)])}
        ]
        pprint.pprint(list(self.collection.aggregate(pipeline)))



# data = MongoDb('java3')
# data.rank_by_occurrence()
# my_query = { "method_name": {"$regex": "^S"} }
# pprint.pprint(data.collection.find_one({"method_name": "setUp"}))


