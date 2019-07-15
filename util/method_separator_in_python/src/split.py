from nltk.tokenize import word_tokenize
from util.method_separator_in_python.src.treat_methods import TreatMethods
from util.extract_code_information import extractor
from util.method_separator_in_python.src.treat_class import TreatClass
from util.method_separator_in_python.src.mongodb import MongoDb

class Split:
    def __init__(self):
        self.treat_methods = TreatMethods()
        self.code_lines = list()
        self.all_methods = list()
        self.stack = list()
        self.class_name = None
        self.line = None
        self.method_name = None
        self.mongodb = MongoDb()

    def work_in_file(self, file):
        with open(file, errors='ignore') as f:
            self.line = f.readline()

            while self.line:
                self.step_management()
                self.line = f.readline()
            f.close()
            return self.all_methods

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
        for i in range(0, len(tokens)):
            if self.treat_methods.check_if_is_usable_method(tokens, self.class_name):
                self.method_name = self.treat_methods.define_method_name(tokens)
                self.code_lines.append(self.line)
                self.stack.append('{')
                break

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
            datas = extractor(self.code_lines.copy())

            json_method = {
                'class_name':self.class_name,
                'method_name':self.method_name,
                'code':' '.join(map(str, self.code_lines.copy())),
                'num_param':datas[0],
                'param_types':datas[1],
                'return_type':datas[2]
            }
            self.mongodb.insert(json_method)
            self.code_lines.clear()
            self.method_name = None
            self.class_name = None


