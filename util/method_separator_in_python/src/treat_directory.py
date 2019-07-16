import os
import re
from split import Split


class TreatDirectory:
    def __init__(self, directory):
        self.directory = directory
        self.receive_objects = list()
        self.count = 0

    def open_and_working_in_directory(self):
        if self.check_directory_existing():
            self.split_java_files_and_add_to_sql(self.directory)

    def split_java_files_and_add_to_sql(self, directory):
        try:
            split = Split()
            for file in os.listdir(directory):
                if os.path.isfile(directory + '/' + file):
                    if self.is_java_file(file):
                        print(self.count)
                        print(directory + '/' + file)
                        self.count += 1
                        self.receive_objects = split.work_in_file(directory + '/' + file)
                else:
                    self.split_java_files_and_add_to_sql(directory + '/' + file)
        except:
            print('ERROR in {}'.format(directory))

    def is_java_file(self, file_name):
        if re.search(".+.java", file_name):
            return True
        return False

    def check_directory_existing(self):
        if not os.path.exists(self.directory):
            print("ERROR. This directory is not available or not exists. ")
            return False
        return True


path = input('Type the directory: ')
TreatDirectory(path).open_and_working_in_directory()