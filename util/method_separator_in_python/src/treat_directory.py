import os
import re
from util.method_separator_in_python.src.split import Split
from code_recommender.src.sqlconnector import MySqlOperator


class TreatDirectory:
    def __init__(self, directory):
        self.directory = directory
        self.receive_objects = list()

    def open_and_working_in_directory(self):
        if self.check_directory_existing():
            self.split_java_files_and_add_to_sql(self.directory)

    def split_java_files_and_add_to_sql(self, directory):
        split = Split()
        for file in os.listdir(directory):
            if os.path.isfile(directory + '/' + file):
                if self.is_java_file(file):
                    self.receive_objects = split.work_in_file(directory + '/' + file)
                    self.treat_methods_to_insert_database()
            else:
                self.split_java_files_and_add_to_sql(directory + '/' + file)

    def treat_methods_to_insert_database(self):
        mysql = MySqlOperator()
        for i in self.receive_objects:
            mysql.insert_table(i.class_name, i.method_name, i.code, i.number_parameters, i.parameter_types, i.return_type)
        mysql.commit_table()

    def is_java_file(self, file_name):
        if re.search(".+.java", file_name):
            return True
        return False

    def check_directory_existing(self):
        if not os.path.exists(self.directory):
            print("ERROR. This directory is not available or not exists. ")
            return False
        return True

