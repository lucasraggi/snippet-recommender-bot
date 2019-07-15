import re
from treat_class import TreatClass

class TreatMethods:
    def check_if_is_usable_method(self, tokens, class_name):
        string = ' '.join(map(str, tokens))
        if re.search('.+\\(?.+\\)?.+{', string) \
                and not self.is_constructor_method(tokens, class_name)\
                and not self.is_main_method(tokens)\
                and not self.is_interface_caller(tokens)\
                and not TreatClass().is_class_caller(tokens):
            return True
        return False

    @staticmethod
    def is_constructor_method(tokens, class_name):
        if class_name in tokens:
            return True
        return False

    @staticmethod
    def is_main_method(tokens):
        string = ' '.join(map(str, tokens))
        if re.search('.+(main|Main).+{', string):
            return True
        return False

    @staticmethod
    def is_interface_caller(tokens):
        if 'interface' in tokens:
            return True
        return False

    @staticmethod
    def define_method_name(tokens):
        for i in range(0, len(tokens)):
            if tokens[i] == '(':
                return tokens[i-1]



