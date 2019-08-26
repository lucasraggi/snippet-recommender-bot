from mongodb import MongoDb
from java_line_remover.find_removable_lines import *
from java_line_remover.find_removable_blocks import *
from java_line_remover.line_remover_main import *
from bson.son import SON
import pprint
import bson

class PreProcess(MongoDb):
    def __init__(self, database_name, collection_name):
        super().__init__(database_name, collection_name)

    def insert_method_by_method_lines(self, document, method_lines, collection_name):
        method = ''
        new_document = document
        for i in method_lines:
            method += i + '\n'
        new_document['_id'] = bson.objectid.ObjectId()
        new_document['code'] = method
        self.db[collection_name].insert_one(new_document)

    def generate_incomplete_methods(self, document, method_lines, valid_lines_to_be_removed, collection_name):
        new_method_lines = []
        method_lines_size = len(method_lines)
        for i in range(method_lines_size):
            if i not in valid_lines_to_be_removed:
                new_method_lines.append(method_lines[i])
        self.insert_method_by_method_lines(document, new_method_lines, collection_name)

    def generate_removed_lines_methods(self, collection_name):
        new_collection = collection_name + '_with_removed_methods'
        self.db[new_collection].drop()
        count = 0
        size = len(self.db[collection_name].find())
        for document in self.db[collection_name].find():
            method = document['code']
            # Getting removable lines
            method_lines = pre_process_method(method)  # Pre processing code (comments, spaces after lines, ...)
            print('##### METHOD i = {} of {} #####'.format(count, size))

            # Getting lines that end with ';
            removable_indexes = get_removable_line_indexes(method_lines)
            # getting for's, if's, while's blocks of lines# '
            removable_block_indexes = get_removable_line_blocks_indexes(method_lines)
            # Getting removable line intervals (ex: 20-30, 15-30, 10-30 )
            valid_lines_to_be_removed = get_removable_indexes_variances(method_lines, removable_indexes, removable_block_indexes)

            # Saving code lines
            self.insert_method_by_method_lines(document, method_lines, new_collection)
            for i in valid_lines_to_be_removed:
                self.generate_incomplete_methods(document, method_lines, i, new_collection)
            self.print_collection(new_collection)
            count += 1

    def rank_by_occurrence(self):
        pipeline = [
            {'$unwind': '$method_name'},
            {'$group': {'_id': '$method_name', 'count': {'$sum': 1}}},
            {'$sort': SON([("count", -1), ("_id", -1)])}
        ]
        aggregate = self.collection.aggregate(pipeline)
        pprint.pprint(list(aggregate))


a = PreProcess('code2algo', 'java1')
a.merge_collections(['java1', 'java2', 'java3', 'java4', 'java5', 'java6'], 'java')
# a.sample_collection_to_another('java1', 'java1_small', 5)
# a.generate_removed_lines_methods('java1_small')
