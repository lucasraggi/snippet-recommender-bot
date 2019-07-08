import re

class TreatClass:
    def define_class_name(self, tokens):
        if self.is_class_type(tokens):
            if self.is_abstract_or_final_class(tokens):
                return tokens[3]
            return tokens[2]

    @staticmethod
    def is_abstract_or_final_class(tokens):
        if 'abstract' in tokens or 'final' in tokens:
            return True
        return False

    @staticmethod
    def is_class_caller(tokens):
        if "class" in tokens:
            return True
        return False

    @staticmethod
    def is_class_type(tokens):
        string = ' '.join(map(str, tokens))
        if re.search('.+class.+{', string):
            return True
        return False




