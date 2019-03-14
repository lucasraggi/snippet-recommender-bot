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


def get_removable_lines(method_lines):
    removable_indexes = []
    size = len(method_lines)
    for index in range(size):
        if method_lines[index][-1:] == ';':
            removable_indexes.append(index)
    return removable_indexes


def main():
    methods = pd.read_csv('result.csv')
    for index, row in methods.iterrows():
        method = row['codes']
        method_lines = pre_process_method(method)
        removable_indexes = get_removable_lines(method_lines)


main()
