import os
import re
from split import Split


class TreatDirectory:
    def __init__(self):
        self.directory = None
        self.split = None
        self.collection = None
        self.receive_objects = list()
        self.count = 0
        self.init = 0

    def setup(self):
        self.directory = input('Type the directory: ')
        self.collection = input('Type the collection name: ')
        self.init = int(input('Type the file number to init: '))
        self.open_and_working_in_directory()

    def open_and_working_in_directory(self):
        if self.check_directory_existing():
            self.split_java_files_and_add_database(self.directory)

    def split_java_files_and_add_database(self, directory):
        try:
            for file in os.listdir(directory):
                if os.path.isfile(directory + '/' + file):
                    if self.is_java_file(file):
                        split = Split(self.collection)
                        split.work_in_file(directory + '/' + file)
                        self.count += 1
                        print(self.count)
                else:
                    self.split_java_files_and_add_database(directory + '/' + file)
        except:
            print('ERROR in {}'.format(directory + '/' + file))

    def is_java_file(self, file_name):
        if re.search(".+.java", file_name):
            return True
        return False

    def check_directory_existing(self):
        if not os.path.exists(self.directory):
            print("ERROR. This directory is not available or not exists. ")
            return False
        return True


TreatDirectory().setup()