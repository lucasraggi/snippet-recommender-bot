from code_identifier.src.code2vec import main
from method_separator_in_python.src.extract_code_information import extractor
from code_recommender.src.recommender import recommender
import json
from flask import Flask


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
    # for i in code_lines:
    #     print(i, end='')
    # print(code_lines[3:5])
    for i in range(len(code_lines)):
        if method in code_lines[i]:
            method_begin, method_end = get_begin_end(code_lines, i)
            method_lines = code_lines[method_begin:method_end + 1]
            return method_lines


app = Flask(__name__)


@app.route("/")
def api():
    json_string = {"_class":"class_test","method":"method_test","code":"package project_test.princ_classes;\n\npublic class class_test {\n\tpublic static void method_test() {\n\t\tint a \u003d 2;\n\t}\n}\n"}
    data_dump = json.dumps(json_string)
    data = json.loads(data_dump)

    method_lines = get_method_lines(data)
    # list_return = main(['--load', '../../models/incomplete_dataset2/saved_model_iter30', '--predict'])
    # print(list_return)
    # method_name = list_return[0]['name']
    method_name = 'nome do metodo'
    number_parameters, types_parameters, return_type = extractor(method_lines)
    json_list = recommender(method_name, number_parameters, types_parameters, return_type)
    print(json_list)
    return 'hello world'


api()
# if __name__ == "__main__":
#     app.run(debug=True)
