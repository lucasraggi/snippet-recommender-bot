import re
from collections import OrderedDict

def get_removable_line_indexes(method_lines):
    removable_indexes = []
    size = len(method_lines)
    for index in range(size):
        if re.search(r'[;][\s]*$', method_lines[index]) is not None:
            removable_indexes.append(index)
    return removable_indexes


def is_first_inside_second(first, second):
    start_first = first[0]
    end_first = first[-1]
    start_second = second[-1]
    end_second = second[0]
    if start_first >= start_second and end_first <= end_second:
        return True
    else:
        return False


# Input: line indexes that end with ';' and list of line blocks of if's, for's
# Output: list of list of removable indexes
def get_removable_indexes_variances(method_lines, removable_indexes, removable_block_indexes):
    method_size = len(method_lines)
    line_number_increment = int(method_size/6)
    curr_variance_size = line_number_increment*2

    lines_to_be_removed = []
    while curr_variance_size < method_size - line_number_increment:  # - line_number_increment to stop before removes the last 5 lines
        temp = []
        for i in range(method_size - 1, curr_variance_size - 1, -1):  # iterating list from method_size to 1
            temp.append(i)
        lines_to_be_removed.append(temp)
        curr_variance_size += line_number_increment
    
    valid_lines_to_be_removed = []  # eliminating only lines that results in a valid method
    for i in range(len(lines_to_be_removed)):
        temp = []
        for j in range(len(removable_block_indexes) - 1, -1, -1):
            if is_first_inside_second(removable_block_indexes[j], lines_to_be_removed[i]):
                temp += removable_block_indexes[j]
        for j in range(len(removable_indexes) - 1, -1, -1):
            if removable_indexes[j] in lines_to_be_removed[i]:
                temp.append(removable_indexes[j])
                temp = list(OrderedDict.fromkeys(valid_lines_to_be_removed))  # eliminate duplicates
                temp.sort(reverse=True)  # sort in reverse order
        valid_lines_to_be_removed.append(temp)
        print(temp)
        print(temp)
        break
    # print(lines_to_be_removed)
    # removable_indexes_list = []  # list of list of removable indexes
    # size = len(removable_indexes)
    # variances_number = 5  # number of removable indexes generated
    # number_lines = int(size / variances_number)
    # for i in range(1, variances_number):
    #     slicing = number_lines * i
    #     removable_indexes_list.append(removable_indexes[slicing:])
    # removable_indexes_list = set(map(tuple, removable_indexes_list))  # removing duplicates from list
    # removable_indexes_list = list(map(list, removable_indexes_list))
    # return removable_indexes_list
