from code_identifier.src.code2vec import main
from code_recommender.src.recommender import recommender
import json


def get_begin_end(code_lines, i):
    method_begin = i
    stack = []
    can_end = False
    for i in range(i, len(code_lines)):
        for j in range(len(code_lines[i])):
            if code_lines[i][j] == '{':
                stack.append('{')
                can_end = True
            if code_lines[i][j] == '}':
                stack.pop()
            if len(stack) == 0 and can_end is True:
                method_end = i
                return method_begin, method_end
    return False, False


def get_method_lines(data):
    method = data['method']
    code_lines = data['code'].splitlines(True)
    for i in code_lines:
        print(i, end='')
    print(code_lines[3:5])
    for i in range(len(code_lines)):
        if method in code_lines[i]:
            method_begin, method_end = get_begin_end(code_lines, i)
            method_lines = code_lines[method_begin:method_end + 1]
            return method_lines


def api():
    json_string = {"_class":"class_test","method":"method_test","code":"package project_test.princ_classes;\n\npublic class class_test {\n\tpublic static void method_test() {\n\t\tint a \u003d 2;\n\t}\n}\n"}
    data_dump = json.dumps(json_string)
    data = json.loads(data_dump)
    get_method_lines(data)
    # list_return = main(['--load', '../models/incomplete_dataset2/saved_model_iter30', '--predict'])
    # print(list_return[0]['name'])


api()
