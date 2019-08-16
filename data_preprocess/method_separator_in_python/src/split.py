from mongodb import MongoDb
from treat_class import TreatClass
from nltk.tokenize import word_tokenize
from treat_methods import TreatMethods


class Split:
    def __init__(self, collection_name):
        self.treat_methods = TreatMethods()
        self.code_lines = list()
        self.stack = list()
        self.class_name = None
        self.line = None
        self.method_name = None
        self.mongodb = MongoDb(collection_name)

    def work_in_file(self, file):
        with open(file, errors='ignore') as f:
            self.line = f.readline()

            while self.line:
                self.step_management()
                self.line = f.readline()
            f.close()

    def step_management(self):
        tokens = word_tokenize(self.line)
        if self.class_name is None:
            self.treat_method_class(tokens)
        else:
            if self.method_name is None:
                self.treat_method(tokens)
            else:
                self.split_methods(tokens)

    def treat_method_class(self, tokens):
        if TreatClass().is_class_caller(tokens):
            self.class_name = TreatClass().define_class_name(tokens)
            self.stack.append('{')

    def treat_method(self, tokens):
        if self.treat_methods.is_method_caller(tokens):
            self.stack.append('{')
            if self.treat_methods.check_if_is_usable_method(tokens, self.class_name):
                self.method_name = self.treat_methods.define_method_name(tokens)
                self.code_lines.append(self.line)

    def split_methods(self, tokens):
        for i in range(0, len(tokens)):
            if i is len(tokens) - 1:
                self.code_lines.append(self.line)
            if tokens[i] is '{':
                self.stack.append('{')
            elif tokens[i] is '}':
                self.stack.pop()
                if len(self.stack) == 0:
                    self.create_new_method_object_and_clear_list()

    def create_new_method_object_and_clear_list(self):
        if len(self.code_lines) > 0:
            json_method = {
                'class_name':self.class_name,
                'method_name':self.method_name,
                'code':' '.join(map(str, self.code_lines.copy())),
            }
            self.mongodb.insert(json_method)
        self.code_lines.clear()
        self.method_name = None
