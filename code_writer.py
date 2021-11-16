from create_function import create_function
from in_out.num_num import num_num
from in_out.num_str import num_str
from in_out.bool_x import bool_x
from in_out.x_bool import x_bool


def code_writer(data):
    type1 = type(data[0][0])
    type2 = type(data[0][1])
    code_list = []

    if type1 == int or type1 == float:
        if type2 == int or type2 == float:
            code_list = num_num(data)

        if type2 == str:
            code_list = num_str(data)

    if type1 == str:
        pass

    if type1 == bool:
        code_list = bool_x(data)

    if type2 == bool:
        code_list = x_bool(data)

    print(code_list)
    create_function(code_list, 'function.py')


data = [
    [4, 2],
    [1, 1],
    [9, 3],
    [100, 10],
    [400, 20]
]

code_writer(data)
