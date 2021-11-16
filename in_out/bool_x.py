def bool_x(data):
    code_list = []
    true_set = False
    false_set = False

    for pair in data:
        # Add condition to true line
        if pair[0] == True and not true_set:
            code_list.append('if input:')
            if type(pair[1]) == str:
                code_list.append(f'    output = "{pair[1]}"')
            else:
                code_list.append(f'    output = {pair[1]}')
                code_list.append('')
            true_set = True

        # Add condition to false line
        elif pair[0] == False and not false_set:
            code_list.append('if not input:')
            if type(pair[1]) == str:
                code_list.append(f'    output = "{pair[1]}"')
            else:
                code_list.append(f'    output = {pair[1]}')
                code_list.append('')
            false_set = True

    return code_list
