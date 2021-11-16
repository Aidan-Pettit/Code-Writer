from create_function import create_function
from math import fabs, sqrt
from all_equal import all_equal
from in_out.num_num import num_num
from in_out.num_str import num_str
from in_out.x_bool import x_bool
from in_out.bool_x import bool_x

data = [
    ['Hello', True],
    ['Bye', True],
    [True, False],
    [0, False]
]

code_list = x_bool(data)
print(code_list)

create_function(code_list, 'function.py')
