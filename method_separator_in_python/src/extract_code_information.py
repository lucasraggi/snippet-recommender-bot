# extract number of parameters, type of parameters, type of return of method




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
