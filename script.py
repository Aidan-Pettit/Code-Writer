from create_function import create_function

finished = False


def iterate_function(count):
    code_list = []

    code_list.append('print(' + str(count) + ')')

    create_function(code_list, 'test' + str(count) + '.py')

    return
