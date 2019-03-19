import re
import pandas as pd


def pre_process_method(lines):
    lines = lines.split('\n')
    lines = filter(lambda x: not re.match(r'^\s*$', x), lines)  # remove whitespaces
    lines = filter(lambda x: not re.match(r'^[\t]*[ ]*//', x), lines)  # remove lines that only have comments
    lines = list(lines)
    for i in range(len(lines)):
        lines[i] = re.sub(r'[ ]*//.*', '', lines[i])  # remove comments like "line of code // comment"
        lines[i] = re.sub(r'[ ]+$', '', lines[i])  # remove spaces after each line
    return lines


def get_removable_line_indexes(method_lines):
    removable_indexes = []
    size = len(method_lines)
    for index in range(size):
        if method_lines[index][-1:] == ';':
            removable_indexes.append(index)
    return removable_indexes


def get_removable_indexes_variances(removable_indexes):
    removable_indexes_list = []  # list of list of removable indexes
    size = len(removable_indexes)
    variances_number = 5  # number of removable indexes generated
    number_lines = int(size / variances_number)
    for i in range(1, variances_number):
        slicing = number_lines*i
        removable_indexes_list.append(removable_indexes[slicing:])
    print(removable_indexes_list)
    for i in range(0, len(removable_indexes_list) - 1):
        if removable_indexes_list[i] == removable_indexes_list[i + 1]:
            del removable_indexes_list[i]
    print(removable_indexes_list)
    print("#############################################")

    return removable_indexes_list


def add_method_by_method_lines(methods, index, method_lines):
    method = ''
    for i in method_lines:
        method += i + '\n'
    methods.append[index, 'codes'] = method


def generate_incomplete_method(methods, method_lines, removable_indexes):
    print(removable_indexes)
    new_method_lines = []
    method_lines_size = len(method_lines)
    for i in range(method_lines_size):
        if i not in removable_indexes:
            new_method_lines.append(method_lines[i])


def main():
    df = pd.read_csv('result.csv')
    methods = df.head(5)
    for index, row in methods.iterrows():
        method = row['codes']
        method_lines = pre_process_method(method)
        removable_indexes = get_removable_line_indexes(method_lines)
        removable_indexes_list = get_removable_indexes_variances(removable_indexes)
        add_method_by_method_lines(methods, index, method_lines)
        methods.drop(index)
        for i in removable_indexes_list:
            generate_incomplete_method(methods, method_lines, i)
        break
    methods.to_csv('results_test.csv', index=False)


main()
