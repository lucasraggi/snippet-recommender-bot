import re

class TreatClass:
    def is_abstract_class(self, tokens):
        if 'abstract' in tokens:
            return True
        return False

    def is_class_caller(self, tokens):
        if "class" in tokens:
            return True
        return False

    def is_class_type(self, tokens):
        string = ' '.join(map(str, tokens))
        if  re.search('(public|private|protected).+{', string):
            return True
        return False

    def define_class_name(self, tokens):
        if self.is_class_type(tokens):
            if self.is_abstract_class(tokens):
                return tokens[3]
            return tokens[2]
        else:
            return tokens[1]

