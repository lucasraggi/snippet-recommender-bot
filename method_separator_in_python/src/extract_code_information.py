# extract number of parameters, type of parameters, type of return of method


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
    return parameter



def extractor():
    file = open('in', 'r')
    code_header = file.readline()
    print(code_header, end='')
    parameter = get_parameters(code_header)  # begin and end of parameters
    if parameter is None:
        return
    number_parameters = get_number_parameters(parameter)
    types_parameters = get_types_parameters(parameter)


extractor()
