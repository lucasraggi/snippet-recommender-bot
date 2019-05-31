import sys
sys.path.append('../..')
from code_identifier.src.code2vec import main
from method_separator_in_python.src.extract_code_information import extractor
from code_recommender.src.recommender import recommender
from datetime import datetime
from werkzeug.serving import run_simple
from flask import Flask
from flask import request
from flask import jsonify
import json
import os


def get_begin_end(code_lines, i):
    method_begin = i
    method_end = 0
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
    while len(stack) > 0:
        code_lines.append('}')
        stack.pop()
    method_end = len(code_lines)
    return method_begin, method_end


def get_method_lines(data):
    method = data['method']
    code_lines = data['code'].splitlines(True)
    print(code_lines)
    for i in range(len(code_lines)):
        if method in code_lines[i]:
            method_begin, method_end = get_begin_end(code_lines, i)
            method_lines = code_lines[method_begin:method_end + 1]
            return method_lines
    return code_lines


to_reload = False


def get_app():
    print("create app now")
    app = Flask(__name__)

    # to make sure of the new app instance
    now = datetime.now()

    @app.route("/")
    def index():
        return "hello, the app started at " + str(now)

    @app.route('/reload')
    def reload():
        global to_reload
        to_reload = True
        return "reloaded"

    # Get json in the format {"_class": ..., "method": ..., "code": ...}
    # Returns json in the format {'method_name': ..., 'method_code': ..., 'method_points': ..., 'num_codes': ...}
    @app.route("/plugin", methods=['POST'])
    def api():
        # json_string = {"_class":"class_test","method":"bubbleSort","code":"public void bubbleSort(int arr[]) {\n         int n = arr.length;\n         for (int i = 0; i < n-1; i++)\n             for (int j = 0; j < n-i-1; j++)\n                 if (arr[j] > arr[j+1])\n                 {\n                     // swap temp and arr[i]\n                     int temp = arr[j];\n                     arr[j] = arr[j+1];\n                     arr[j+1] = temp;\n                 }\n     }\n', '1', 'int', 'void'"}
        json_string = request.get_json()
        data_dump = json.dumps(json_string)
        data = json.loads(data_dump)
        print("Codigo: \n", data['code'])
        method_lines = get_method_lines(data)
        print(method_lines)
        # for i in method_lines:
        #     print(i, end='')
        f = open('Input.java', 'w')
        for i in method_lines:
            f.write(i)
        f.close()
        list_return = main(['--load', '../../models/incomplete_dataset2/saved_model_iter30', '--predict'])
        method_name = list_return[0]['name']
        method_name = ''.join(method_name)
        number_parameters, types_parameters, return_type = extractor(method_lines)
        json_dict = recommender(method_name, number_parameters, types_parameters, return_type)
        print(json_dict['method_code'])
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
        print(method_name)
        number_parameters, types_parameters, return_type = extractor(method_lines)
        json_dict = recommender(method_name, number_parameters, types_parameters, return_type)
        method_code = json_dict['method_code']
        print(method_code)
        if len(method_code) > 0:
            method_code = method_code[0]
        response = jsonify(method_code)
        print(response)
        return response

        # Get string with the incomplete code snippet
        # Returns string with the best fitting algorithm code
    @app.route("/code_name", methods=['POST'])
    def api_name():
        alg_name = request.get_data()
        alg_name = str(alg_name.decode('utf-8'))
        number_parameters, types_parameters, return_type = 0, [], ''
        json_dict = recommender(alg_name, number_parameters, types_parameters, return_type)
        method_code = json_dict['method_code']
        print(method_code)
        if len(method_code) > 0:
            method_code = method_code[0]
        response = jsonify(method_code)
        print(response)
        return response

    @app.route("/test", methods=['POST'])
    def api_test():
        print(request.is_json)
        content = request.get_json()
        method_name_list = ['bubbleSort']
        method_code_list = [
            'static void bubbleSort(int[] arr) {  \n' '        int n = arr.length;  \n' '        int temp = 0;  \n' '         for(int i=0; i < n; i++){  \n' '                 for(int j=1; j < (n-i); j++){  \n' '                          if(arr[j-1] > arr[j]){  \n' '                                 //swap elements  \n' '                                 temp = arr[j-1];  \n' '                                 arr[j-1] = arr[j];  \n' '                                 arr[j] = temp;    \n' '                                 \n' '                         } \n' '                 }  \n' '         }  \n' '  \n' '    ']
        method_points_list = ['2']

        method_dict = {'method_name': method_name_list,
                       'method_code': method_code_list,
                       'method_points': method_points_list,
                       'num_codes': '1'}
        print(method_dict)
        response = jsonify(method_dict)
        return response

    return app


class AppReloader(object):
    def __init__(self, create_app):
        self.create_app = create_app
        self.app = create_app()

    def get_application(self):
        global to_reload
        if to_reload:
            self.app = self.create_app()
            to_reload = False

        return self.app

    def __call__(self, environ, start_response):
        app = self.get_application()
        return app(environ, start_response)


# This application object can be used in any WSGI server
# for example in gunicorn, you can run "gunicorn app"
application = AppReloader(get_app)


if __name__ == '__main__':
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)
