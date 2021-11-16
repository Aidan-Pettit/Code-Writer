from re import search, sub


def str_str(data):
    code_list = []
    pair = []
    unincluded = []
    conditions = []

    if data[0] == data[1]:
        code_list.append('output = input')
        return code_list

    for _pair in data:
        if _pair[0][-1] == 1:
            pass

    for _pair in data:

        for char in _pair[0]:
            if not search(char, _pair[1]):
                unincluded.append(char)
