import sys


def work_with_variables(variable, num, variables_map):
    variable_value = variables_map.get(variable)
    if not variable_value:
        variables_map[variable] = num
    else:
        if variable_value != num:
            raise Exception

def get_type(num):
    if num.isalpha():
        return 'str'
    else:
        return 'int'


def play_with_array(length: int, array_1: list, array_2: list):
    var_map = {}
    var_tuples = []
    try:
        for i in range(length):
            num_1 = array_1[i]
            num_2 = array_2[i]
            num_1_type = get_type(num_1)
            num_2_type = get_type(num_2)
            if num_1_type == 'int' and num_2_type == 'int':
                if num_1 != num_2:
                    raise Exception
            elif num_1_type == 'str' and num_2_type == 'int':
                work_with_variables(num_1, num_2, var_map)
            elif num_1_type == 'int' and num_2_type == 'str':
                work_with_variables(num_2, num_1, var_map)
            elif num_1_type == 'str' and num_2_type == 'str':
                if num_1_type == num_2_type:
                    continue
                else:
                    var_tuples.append((num_1, num_2))
        if var_tuples:
            for var_tuple in var_tuples:
                var_value_1 = var_map.get(var_tuple[0])
                var_value_2 = var_map.get(var_tuple[1])
                if var_value_1 is None and var_value_2:
                    var_map[var_tuple[0]] = var_value_2
                elif var_value_2 is None and var_value_1:
                    var_map[var_tuple[1]] = var_value_1
                else:
                    if var_value_1 != var_value_2:
                        raise Exception
    except Exception:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    stdin = sys.stdin
    length = int(stdin.readline())
    array_1 = [x for x in stdin.readline().split()]
    array_2 = [x for x in stdin.readline().split()]
    print(play_with_array(length, array_1, array_2))
