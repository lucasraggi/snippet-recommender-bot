import os
import re
from file_split_management import Split
from mysql_connector import MySqlOperator
from treat_code2vec_dataset import treat_code2vec_database

class TreatDirectory:
    def __init__(self, directory):
        self.directory = directory
        self.cout = 0

    def open_and_working_in_directory(self):
        if self.check_directory_existing():
            self.split_java_files_and_add_to_sql(self.directory)

    def split_java_files_and_add_to_sql(self, directory):
        mysql_operator = MySqlOperator()
        receive_objects = list()
        common_methods = treat_code2vec_database()
        split = Split(common_methods)

        for file in os.listdir(directory):
            try:
                if os.path.isfile(directory + '/' + file):
                    if self.is_java_file(file):
                        self.cout += 1
                        receive_objects = split.work_in_file(directory + '/' + file)
                        mysql_operator.insert_table(receive_objects)
                        receive_objects.clear()

                    if self.cout % 1000 == 0:
                        print('Commit in table - 1k')
                        mysql_operator.commit_table()
                        mysql_operator.reset_query_cache()
                else:
                    self.split_java_files_and_add_to_sql(directory + '/' + file)
            except:
                print(directory + '/' + file)

        mysql_operator.commit_table()
        mysql_operator.close_connection()

    def is_java_file(self, file_name):
        if re.search(".+.java", file_name):
            return True
        return False

    def check_directory_existing(self):
        if not os.path.exists(self.directory):
            print("ERROR. This directory is not available or not exists. ")
            return False
        return True
