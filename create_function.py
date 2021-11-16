from stringify_code_list import stringify_code_list


def create_function(code_list, filename):
    code = stringify_code_list(code_list)

    file = open(filename, 'w')
    file.write(code)
