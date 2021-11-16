def x_bool(data):
    code_list = []
    true_values = []
    false_values = []
    true_line = 'if '
    false_line = 'if '

    for pair in data:
        if pair[1] == True:
            true_values.append(pair[0])
        elif pair[1] == False:
            false_values.append(pair[0])

    index = 1

    for value in true_values:
        if type(value) == str:
            true_line += f'input == "{value}"'
        else:
            true_line += f'input == {value}'

        if not index == len(true_values):
            true_line += ' or '

        index += 1

    true_line += ':'
    index = 1

    for value in false_values:
        if type(value) == str:
            false_line += f'input == "{value}"'
        else:
            false_line += f'input == {value}'

        if not index == len(false_values):
            false_line += ' or '

        index += 1

    false_line += ':'

    code_list.append(true_line)
    code_list.append('    output = True')
    code_list.append('')

    code_list.append(false_line)
    code_list.append('    output = False')
    code_list.append('')

    # for pair in data:
    #     if pair[1] == True:
    #         line += f'input == {pair[0]} '

    #     if not index == len(data):
    #         line += ' or '

    #     index += 1

    # line += ':'

    # code_list.append(line)
    # code_list.append('    output = True')

    # line = 'if '

    # index = 1

    # for pair in data:
    #     if pair[1] == False:
    #         line += f'input == {pair[0]} '

    #         if not index == len(data):
    #             line += ' or '

    #     index += 1

    # line += ':'

    # code_list.append(line)
    # code_list.append('    output = False')

    return code_list
