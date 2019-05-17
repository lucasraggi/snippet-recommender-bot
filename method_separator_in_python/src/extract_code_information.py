# extract number of parameters, type of parameters


def get_parameters(code_header):
    begin = -1
    end = -1
    for i in range(0, len(code_header)):
        if code_header[i] == '(':
            begin = i
    for i in reversed(range(0, len(code_header))):
        if code_header[i] == ')':
            end = i
    if begin == -1 or end == -1:
        parameter = None
    else:
        parameter = code_header[begin + 1:end]
    return parameter, begin, end


def get_number_parameters(parameters):
    number_parameters = len(parameters.split(','))
    return number_parameters


def get_types_parameters(parameter):
    types_parameters = []
    parameters = parameter.split(',')
    for param in parameters:
        temp = param.lstrip()  # remove whitespace, tab and newline from begin of string
        temp = temp.rstrip()  # remove whitespace, tab and newline from end of string
        temp = temp.split(' ')  # separate string by space
        types_parameters.append(temp[0])  # temp[0] is var type and temp[1] is var name
    return types_parameters


def get_return_type(code_header, begin):
    if begin == -1:
        return
    print(code_header)
    

def extractor(method_lines):
    # file = open('in', 'r')
    # code_header = file.readline()
    code_header = method_lines[0]
    parameter, begin, end = get_parameters(code_header)  # begin and end of parameters
    if parameter is None:
        return
    number_parameters = get_number_parameters(parameter)
    types_parameters = get_types_parameters(parameter)
    return_type = get_return_type(code_header, begin)
    return number_parameters, types_parameters, return_type


# extractor()
