import pymongo
import pymongo.errors
from pymongo import MongoClient
import re
import os
import pprint
import bson

class MongoDb:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.collection_name = collection_name
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

    def delete_collection(self, collection_name):
        self.db.drop_collection(collection_name)

    def delete_all_data(self):
        self.collection.delete_many({})

    def delete_list_by_key(self, key, list_to_remove):
        list_to_remove = ['\\b' + item + '\\b' for item in list_to_remove]
        regex = '|'.join(list_to_remove)
        query = {key: re.compile(regex)}
        x = self.collection.find(query)
        print(x.count())
        y = self.collection.delete_many(query)
        print(y.deleted_count, " documents deleted.")
        x = self.collection.find(query)
        print(x.count())

    def clone_collection(self, original_collection, destination_collection):
        pipeline = [{"$match": {}},
                    {"$out": destination_collection},
                    ]
        self.db[original_collection].aggregate(pipeline)

    def merge_collections(self, collection_name_list, merged_collection_name):
        new_collection = self.db[merged_collection_name]
        new_collection.drop()
        for collection in collection_name_list:
            self.db[collection].aggregate([{"$merge": merged_collection_name}])
            print('Collection {} Done'.format(collection))
            break

    def sample_collection_to_another(self, source_collection, destination_collection, n_samples):
        count = 0
        for document in self.db[source_collection].find():
            self.db[destination_collection].insert_one(document)
            if count >= n_samples:
                break
            count += 1

    def print_collection(self, collection_name, n=10):
        count = 0
        for document in self.db[collection_name].find():
            print('####################### METHOD:', count, '#######################')
            print(document['code'])
            if count >= n:
                break
            count += 1

    def export_to_java_files(self):
        count = 0
        directory_path = '../java_files'
        os.makedirs(directory_path, exist_ok=True)
        os.chdir(directory_path)  # setting working directory to path
        start = 0
        file_count = start
        for document in self.collection.find():
            file_name = str(file_count) + '.java'
            f = open(file_name, 'w+')
            method_name = document['method_name']
            file_start_string = 'public class ' + str(method_name) + ' {\n\n'
            method = document['code']
            file_end_string = '\n}'
            string_to_file = file_start_string + str(method) + file_end_string
            f.write(string_to_file)
            f.close()
            file_count += 1
            # count += 1
            # if count >= 5:
            #     break


data = MongoDb('code2algo', 'java1')
# data.sample_collection_to_another('java1', 'java1_sample', 20)
data.merge_collections(['java1', 'java2', 'java3', 'java4', 'java5', 'java6'], 'java')
# data.rank_by_occurrence()
# list_to_remove = ['bubbleSort', 'DFS', 'InsertionSort']
# alg_list = ['getType', 'toObject']
# data.delete_list_by_key('method_name', alg_list)
# data.export_to_java_files()
# my_query = { "method_name": {"$regex": "^S"} }
# pprint.pprint(data.collection.find_one({"method_name": "setUp"}))


