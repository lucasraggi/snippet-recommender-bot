import os
import re
import pandas as pd


def pre_process_method(lines):
    lines = lines.split('\n')
    lines = filter(lambda x: not re.match(r'^\s*$', x), lines)  # remove whitespaces
    lines = filter(lambda x: not re.match(r'^[\t]*[ ]*//', x), lines)  # remove lines that only have comments
    lines = list(lines)
    for i in range(len(lines)):
        lines[i] = re.sub(r'[ ]*//.*', '', lines[i])
    return lines


def separate_removable_lines(method_lines):
    pass

def main():
    methods = pd.read_csv('result.csv')
    for index, row in methods.iterrows():
        method = row['codes']
        method_lines = pre_process_method(method)
        separate_removable_lines(method_lines)
        break


main()