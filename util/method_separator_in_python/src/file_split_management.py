from nltk.tokenize import word_tokenize
from util.method_separator_in_python.src.treat_methods import TreatMethods
from util.method_separator_in_python.src.extract_code_information import extractor

class JavaMethod:
    def __init__(self, class_name, method_name, code, number_parameters, parameter_types, return_type):
        self.class_name = class_name
        self.method_name = method_name
        self.code = code
        self.number_parameters = number_parameters
        self.parameter_types = parameter_types
        self.return_type = return_type


class Split:
    def __init__(self):
        self.treat_methods = TreatMethods()
        self.code_lines = list()
        self.all_methods = list()
        self.stack = list()
        self.class_name = None
        self.line = None
        self.method_name = None

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

        if self.method_name is None:
            self.treat_method(tokens)
        else:
            self.split_methods(tokens)

    def treat_method_class(self, tokens):
        if self.treat_class.is_class_caller(tokens):
            name = self.treat_class.define_class_name(tokens)
            self.class_name = name

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
        datas = extractor(self.code_lines.copy())
        code = ' '.join(map(str, self.code_lines.copy()))
        num_param = datas[0]
        param_types = ' '.join(map(str, datas[1]))
        return_type = datas[2]
        new_method = JavaMethod(self.class_name, self.method_name, code, num_param, param_types, return_type)
        self.all_methods.append(new_method)
        self.code_lines.clear()


