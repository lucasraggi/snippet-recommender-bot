import pcre
import re


def print_removable_blocks(removable_line_blocks):
    print('[', end='')
    for i in removable_line_blocks:
        print('[', i[0], '-', i[-1], ']', end='')
    print(']')


def get_non_overlapping_blocks_indexes(removable_line_blocks):  # get only the outside for's and if's
    size = len(removable_line_blocks)
    outside_blocks_indexes = []
    inside_blocks_indexes = []
    for i in range(size):
        if i in inside_blocks_indexes:
            continue
        start1 = removable_line_blocks[i][0]
        end1 = removable_line_blocks[i][-1]
        # print(start1, ' ', end1)
        for j in range(i + 1, size):
            start2 = removable_line_blocks[j][0]
            end2 = removable_line_blocks[j][-1]
            if start1 < start2 and end1 > end2:
                if i not in outside_blocks_indexes:
                    outside_blocks_indexes.append(i)
                inside_blocks_indexes.append(j)
            else:
                break
            # print('     ', start2, ' ', end2)
    print(outside_blocks_indexes)
    print('[[ 11 - 30 ][ 19 - 30 ]]')


def get_removable_line_blocks_indexes(method_lines):  # get removable lines of for's and if's
    if_begin_regex = pcre.compile(
        r"if\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    elif_begin_regex = pcre.compile(
        r"else if\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    for_begin_regex = pcre.compile(
        r"for\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    while_begin_regex = pcre.compile(
        r"while\s*\(((?:(?:(?:\"(?:(?:\\\")|[^\"])*\")|(?:'(?:(?:\\')|[^'])*'))|[^\(\)]|\((?1)\))*)\)")
    with open("../in", "r") as file:
        method_lines = file.readlines()
    size = len(method_lines)
    removable_line_blocks = []
    jump_line = 0
    for i in range(size):
        # checks if the line has a for or if
        if jump_line > 0:
            jump_line -= 1
            continue
        if for_begin_regex.search(method_lines[i]) is not None or if_begin_regex.search(method_lines[i]) is not None or elif_begin_regex.search(method_lines[i]) is not None or while_begin_regex.search(method_lines[i]) is not None:
            balancing_stack = []
            quotation_stack = []
            double_quotation_stack = []
            can_end = False
            removable_line_block = []
            # print('CURRENT FOR or IF: ')
            temp = i
            while if_begin_regex.search(method_lines[temp]) is not None and if_begin_regex.search(method_lines[temp + 1]) is not None:  # chained one line if (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            while elif_begin_regex.search(method_lines[temp]) is not None and elif_begin_regex.search(method_lines[temp + 1]) is not None:  # chained one line for (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            while for_begin_regex.search(method_lines[temp]) is not None and for_begin_regex.search(method_lines[temp + 1]) is not None:  # chained one line for (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            while while_begin_regex.search(method_lines[temp]) is not None and while_begin_regex.search(method_lines[temp + 1]) is not None:  # chained one line for (recursive)
                # print('##############\nwhile loop\n', method[temp], method[temp + 1], '###################')
                jump_line += 1
                temp += 1
            for j in range(i, size):
                #  print('     i = ', i, 'CURR LINE: ', method[j], end='')
                if len(balancing_stack) == 0 and can_end is True:
                    break
                if j > i + 1 and can_end is False and len(balancing_stack) == 0 and re.search(r'[;][\s]*$', method_lines[i + 1]) is not None:  # one line for or if without '{ }"
                    break
                removable_line_block.append(j + 1)  # +1 because the lines start with 1 and index with 0

                for k in method_lines[j]:
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
    #get_non_overlapping_blocks_indexes(removable_line_blocks)
    return removable_line_blocks
