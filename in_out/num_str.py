def num_str(data):
    code_list = []
    pair = data[0]

    if str(pair[0]) == pair[1]:
        return [f"output = str(input)"]

    if str(pair[0]) == pair[1][0]:
        return [f"output = str(input) * input"]

    if len(pair[1]) == pair[0]:
        return [f"output = '{pair[1][0]}' * input"]

    for _pair in data:
        code_list.append(
            f"if input == {_pair[0]}:\n        output = '{_pair[1]}'\n")

    return code_list
