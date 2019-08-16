from mongodb import MongoDb
from java_line_remover.find_removable_lines import *
from java_line_remover.find_removable_blocks import *
from java_line_remover.line_remover_main import *


class PreProcess(MongoDb):
    def __init__(self, collection_name):
        super().__init__(collection_name)

    def generate_removed_lines_methods(self):
        new_collection = self.collection_name + '_with_removed_methods'
        for document in self.db[new_collection].find():
            method = document['codes']
            # Getting removable lines
            method_lines = pre_process_method(method)  # Pre processing code (comments, spaces after lines, ...)
            print('##### METHOD i = {} ############################################################'.format(index))
            print_method_lines(method_lines)

            removable_indexes = get_removable_line_indexes(method_lines)  # Getting lines that end with ';'
            removable_block_indexes = get_removable_line_blocks_indexes(
                method_lines)  # getting for's, if's, while's blocks of lines
            valid_lines_to_be_removed = get_removable_indexes_variances(method_lines, removable_indexes,
                                                                        removable_block_indexes)  # Getting removable line variances (ex: 20-30, 15-30, 10-30 )
            # Saving code lines
            current_method = methods.loc[index]
            methods = methods.drop(index)
            methods = add_method_by_method_lines(methods, current_method, method_lines)
            for i in valid_lines_to_be_removed:
                methods = generate_incomplete_method(methods, current_method, method_lines, i)
        methods = methods.sample(frac=1).reset_index(drop=True)  # Shuffle rows
        methods = methods.drop('index', axis=1)
        methods.to_csv('../results_variances.csv')



a = PreProcess('java')
a.clone_collection('java', 'java_test')
