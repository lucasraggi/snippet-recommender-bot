import re
import pandas as pd
import pcre


def print_method_lines(method_lines):
    for i in method_lines:
        print(i)


def pre_process_method(lines):
    lines = lines.split('\n')
    lines = filter(lambda x: not re.match(r'^\s*$', x), lines)  # remove whitespaces after line
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
        if re.search(r'[;][\s]*$', method_lines[index]) is not None:
            removable_indexes.append(index)
    return removable_indexes


def print_removable_blocks(removable_line_blocks):
    print('[', end='')
    for i in removable_line_blocks:
        print('[', i[0], '-', i[-1], ']', end='')
    print(']')


def get_removable_line_blocks_indexes(method_lines):
    if_begin_regex = pcre.compile(
        r"if\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    for_begin_regex = pcre.compile(
        r"for\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    with open("../in", "r") as file:
        method = file.readlines()
    size = len(method)
    removable_line_blocks = []
    jump_line = 0
    for i in range(size):
        # checks if the line has a for or if
        if jump_line > 0:
            jump_line -= 1
            continue
        if for_begin_regex.search(method[i]) is not None or if_begin_regex.search(method[i]) is not None:
            balancing_stack = []
            quotation_stack = []
            double_quotation_stack = []
            can_end = False
            removable_line_block = []
            # print('CURRENT FOR or IF: ')
            temp = i
            while if_begin_regex.search(method[temp + 1]) is not None:  # chained one line if (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            while for_begin_regex.search(method[temp + 1]) is not None:  # chained one line for (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            for j in range(i, size):
                #  print('     i = ', i, 'CURR LINE: ', method[j], end='')
                if len(balancing_stack) == 0 and can_end is True:
                    break
                if j > i + 1 and can_end is False and len(balancing_stack) == 0 and re.search(r'[;][\s]*$', method[i + 1]) is not None:  # one line for or if without '{ }"
                    break
                removable_line_block.append(j + 1)  # +1 because the lines start with 1 and index with 0

                for k in method[j]:
                    if len(quotation_stack) == 0 and len(double_quotation_stack) == 0:  # if its not inside string, can add
                        can_add = True
                    else:
                        can_add = False
                    if k == '\'' and len(quotation_stack) == 0:  # checks if '{' is inside string ex: a = " { "
                        quotation_stack.append('\'')
                    elif k == '\'' and len(quotation_stack) > 0:
                        quotation_stack.pop()
                    if k == '\"' and len(quotation_stack) == 0:
                        double_quotation_stack.append('\'')
                    elif k == '\"' and len(quotation_stack) > 0:
                        double_quotation_stack.pop()

                    if k == '{' and can_add:
                        # print('         before push: ', balancing_stack)
                        balancing_stack.append('{')
                        can_end = True
                        # print('         after push: ', balancing_stack)
                    if k == '}' and len(balancing_stack) > 0 and can_add:
                        # print('         before pop: ', balancing_stack)
                        balancing_stack.pop()
                        # print('         after pop: ', balancing_stack)

            removable_line_blocks.append(removable_line_block)
    # print(removable_line_blocks)
    print_removable_blocks(removable_line_blocks)


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


def add_method_by_method_lines(methods, current_method, method_lines):
    method = ''
    for i in method_lines:
        method += i + '\n'
    current_method.at['codes'] = method
    methods = methods.append(current_method)
    return methods


def generate_incomplete_method(methods, current_method, method_lines, removable_indexes):
    new_method_lines = []
    method_lines_size = len(method_lines)
    for i in range(method_lines_size):
        if i not in removable_indexes:
            new_method_lines.append(method_lines[i])
    methods = add_method_by_method_lines(methods, current_method, new_method_lines)
    return methods


def main():
    get_removable_line_blocks_indexes('test')
    # df = pd.read_csv('./result.csv')
    # methods = df.head(5)
    # methods = methods.drop('id', axis=1)
    # for index, row in methods.iterrows():
    #     method = row['codes']
    #     method_lines = pre_process_method(method)
    #     removable_indexes = get_removable_line_indexes(method_lines)
    #     removable_indexes_list = get_removable_indexes_variances(removable_indexes)
    #     current_method = methods.loc[index]
    #     methods = methods.drop(index)
    #     methods = add_method_by_method_lines(methods, current_method, method_lines)
    #     for i in removable_indexes_list:
    #         methods = generate_incomplete_method(methods, current_method, method_lines, i)
    # methods = methods.reset_index()
    # methods = methods.drop('index', axis=1)
    # methods.to_csv('results_test.csv')


main()
