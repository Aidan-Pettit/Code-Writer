from re import search


def stringify_code_list(code_list):
    code = 'def test(input):\n    output = None\n\n'

    for line in code_list:
        code += '    ' + line + '\n'

    code += '\n' + '    return output'

    # if search('fabs', code):
    #     code += 'fabs\n\n' + code

    return code
