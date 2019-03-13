import os
import re
import pandas as pd


def separate_valid_lines(method):
    lines = method.split('\n')
    for line in lines:
        print(line)


def main():
    methods = pd.read_csv('result.csv')
    for index, row in methods.iterrows():
        # print(row['codes'])
        separate_valid_lines(row['codes'])
        break


main()