import re


def get_removable_line_indexes(method_lines):
    removable_indexes = []
    size = len(method_lines)
    for index in range(size):
        if re.search(r'[;][\s]*$', method_lines[index]) is not None:
            removable_indexes.append(index)
    return removable_indexes


def get_removable_indexes_variances(removable_indexes):
    removable_indexes_list = []  # list of list of removable indexes
    size = len(removable_indexes)
    variances_number = 5  # number of removable indexes generated
    number_lines = int(size / variances_number)
    for i in range(1, variances_number):
        slicing = number_lines * i
        removable_indexes_list.append(removable_indexes[slicing:])
    removable_indexes_list = set(map(tuple, removable_indexes_list))  # removing duplicates from list
    removable_indexes_list = list(map(list, removable_indexes_list))
    return removable_indexes_list
