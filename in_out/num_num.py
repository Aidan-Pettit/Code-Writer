from math import sqrt, fabs
from all_equal import all_equal


def num_num(data):
    code_list = []
    storage = []

    for pair in data:
        result = pair[0] - pair[1]
        storage.append(result)

    if all_equal(storage) and not storage[0] == 0:
        operator = '+' if storage[0] < 0 else '-'
        code_list.append(
            f'output = input {operator} {str(int(fabs(storage[0])))}')

    storage = []

    for pair in data:
        result = pair[0] / pair[1]
        storage.append(result)

    if all_equal(storage):
        code_list.append(f'output = input * {str(1 / storage[0])}')

    storage = []

    for pair in data:
        result = pair[0] ** 2
        storage.append(result)

    if data[0][1] == storage[0]:
        code_list.append(f'output = input ** 2')

    storage = []

    for pair in data:
        if pair[0] < 0:
            break
        result = sqrt(pair[0])
        storage.append(result)

    if data[0][1] == storage[0]:
        code_list.append(f'output = sqrt(input)')

    storage = []

    for pair in data:
        result = fabs(pair[0])
        storage.append(result)

    if data[0][1] == storage[0]:
        code_list.append(f'output = fabs(input)')

    storage = []

    return code_list


def all_equal(list):
    allEqual = True

    for result in list:
        isEqual = result == list[0]
        if not isEqual:
            allEqual = False

    return allEqual
