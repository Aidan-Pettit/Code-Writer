def bool_bool(data):
    code_list = []

    if data[0] == data[1]:
        code_list.append('output = input')
    else:
        code_list.append('output = not input')
