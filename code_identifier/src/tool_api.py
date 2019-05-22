import sys
sys.path.append('../..')
from code_identifier.src.code2vec import main
from method_separator_in_python.src.extract_code_information import extractor
from code_recommender.src.recommender import recommender
import json
import os
from flask import Flask
from flask import request
from flask import jsonify


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
    for i in range(len(code_lines)):
        if method in code_lines[i]:
            method_begin, method_end = get_begin_end(code_lines, i)
            method_lines = code_lines[method_begin:method_end + 1]
            return method_lines


app = Flask(__name__)


# Get json in the format {"_class": ..., "method": ..., "code": ...}
# Returns json in the format {'method_name': ..., 'method_code': ..., 'method_points': ..., 'num_codes': ...}
@app.route("/plugin", methods=['POST'])
def api():
    # json_string = {"_class":"class_test","method":"bubbleSort","code":"public void bubbleSort(int arr[]) {\n         int n = arr.length;\n         for (int i = 0; i < n-1; i++)\n             for (int j = 0; j < n-i-1; j++)\n                 if (arr[j] > arr[j+1])\n                 {\n                     // swap temp and arr[i]\n                     int temp = arr[j];\n                     arr[j] = arr[j+1];\n                     arr[j+1] = temp;\n                 }\n     }\n', '1', 'int', 'void'"}
    json_string = request.get_json()
    data_dump = json.dumps(json_string)
    data = json.loads(data_dump)
    method_lines = get_method_lines(data)
    print(method_lines)
    f = open('Input.java', 'w')
    for i in method_lines:
        f.write(i)
    f.close()
    list_return = main(['--load', '../../models/incomplete_dataset2/saved_model_iter30', '--predict'])
    method_name = list_return[0]['name']
    method_name = ''.join(method_name)
    number_parameters, types_parameters, return_type = extractor(method_lines)
    json_dict = recommender(method_name, number_parameters, types_parameters, return_type)
    response = jsonify(json_dict)
    return response


# Get string with the incomplete code snippet
# Returns string with the best fitting algorithm code
@app.route("/code", methods=['POST'])
def api_method():
    # json_string = {"_class":"class_test","method":"bubbleSort","code":"public void bubbleSort(int arr[]) {\n         int n = arr.length;\n    "}
    method_lines = request.get_data()
    method_lines = str(method_lines.decode('utf-8'))
    method_lines = method_lines.splitlines(True)
    f = open('Input.java', 'w')
    for i in method_lines:
        f.write(i)
    f.close()
    list_return = main(['--load', '../../models/incomplete_dataset2/saved_model_iter30', '--predict'])
    method_name = list_return[0]['name']
    method_name = ''.join(method_name)
    number_parameters, types_parameters, return_type = extractor(method_lines)
    json_dict = recommender(method_name, number_parameters, types_parameters, return_type)
    method_code = json_dict['method_code']
    method_code = method_code[0]
    response = jsonify(method_code)
    print(response)
    return response


@app.route("/test", methods=['POST'])
def api_test():
    print(request.is_json)
    content = request.get_json()
    response = jsonify(content)
    return response


if __name__ == "__main__":
    app.run(debug=True)
