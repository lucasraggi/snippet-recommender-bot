import os
import re
from src.file_split_management import Split
from src.mysql_connector import MySqlOperator

class TreatDirectory:
    def __init__(self, directory):
        self.directory = directory

    def open_and_working_in_directory(self):
        if self.check_directory_existing():
            self.split_java_files_and_add_to_sql(self.directory)

    def split_java_files_and_add_to_sql(self, directory):
        split = Split()
        mysql_operator = MySqlOperator()
        receive_objects = list()

        try:
            for file in os.listdir(directory):
                if os.path.isfile(directory + '/' + file):
                    if self.is_java_file(file):
                        receive_objects = split.work_in_file(directory + '/' + file)
                        mysql_operator.insert_table(receive_objects)
                        receive_objects.clear()
                else:
                    self.split_java_files_and_add_to_sql(directory + '/' + file)
            mysql_operator.commit_table()
        except:
            print("ERROR in directory " + directory)

    def is_java_file(self, file_name):
        if re.search("\w.+.java", file_name):
            return True
        return False

    def check_directory_existing(self):
        if not os.path.exists(self.directory):
            print("ERROR. This directory is not available or not exists. ")
            return False
        return True
