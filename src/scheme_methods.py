import sys
from inspect import currentframe, getframeinfo


def validate_numbers(arg_list):
    for element in arg_list:
        if not isinstance(element, int) and not isinstance(element, float):
            sys.exit('\n\nTypeError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', unexpected type. There should be numeric arguments')
    return True


def op_add(arg_list):
    validate_numbers(arg_list)
    res = 0
    for i in arg_list:
        res = res + i
    return res


def op_sub(arg_list):
    validate_numbers(arg_list)
    res = arg_list[0]
    for i in range(1, len(arg_list)):
        res = res - arg_list[i]
    return res


def op_mul(arg_list):
    validate_numbers(arg_list)
    res = 1
    for i in arg_list:
        res = res * i
    return res


def op_truediv(arg_list):
    validate_numbers(arg_list)
    res = arg_list[0]
    for i in range(1, len(arg_list)):
        if arg_list[i] == 0:
            sys.exit('\n\nZeroDivisionError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', float division by zero')
        res = res / arg_list[i]
    return res


def op_gt(arg_list):
    validate_numbers(arg_list)
    for i in range(1, len(arg_list)):
        if arg_list[0] <= arg_list[i]:
            return False
    return True


def op_lt(arg_list):
    validate_numbers(arg_list)
    for i in range(1, len(arg_list)):
        if arg_list[0] >= arg_list[i]:
            return False
    return True


def op_ge(arg_list):
    validate_numbers(arg_list)
    for i in range(1, len(arg_list)):
        if arg_list[0] < arg_list[i]:
            return False
    return True


def op_le(arg_list):
    validate_numbers(arg_list)
    for i in range(1, len(arg_list)):
        if arg_list[0] > arg_list[i]:
            return False
    return True


def op_eq(arg_list):
    validate_numbers(arg_list)
    for i in range(1, len(arg_list)):
        if arg_list[0] != arg_list[i]:
            return False
    return True


def eq_ref_ch(arg_list):
    for i in range(1, len(arg_list)):
        if id(arg_list[0]) != id(arg_list[i]):
            return False
    return True


def equal_ch(arg_list):
    for i in range(1, len(arg_list)):
        if arg_list[0] != arg_list[i]:
            return False
    return True


def op_abs(arg_list):
    validate_numbers(arg_list)
    if arg_list[0] < 0:
        return -1 * arg_list[0]
    else:
        return arg_list[0]


def max_f(arg_list):
    validate_numbers(arg_list)
    max = arg_list[0]
    for i in range(1, len(arg_list)):
        if max < arg_list[i]:
            max = arg_list[i]
    return max


def min_f(arg_list):
    validate_numbers(arg_list)
    minimum = arg_list[0]
    for i in range(1, len(arg_list)):
        if minimum > arg_list[i]:
            minimum = arg_list[i]
    return minimum


def and_f(arg_list):
    if len(arg_list) < 2:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "and" method')
    for el in arg_list:
        if type(el) != bool:
            sys.exit('\n\nTypeError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', the types of arguments passed to "and" method should be boolean')
    for el in arg_list:
        if not el:
            return False
    return True


def or_f(arg_list):
    if len(arg_list) < 2:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "or" method')
    for el in arg_list:
        if type(el) != bool:
            sys.exit('\n\nTypeError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', the types of arguments passed to "or" method should be boolean')
    for el in arg_list:
        if el:
            return True
    return False


def not_f(arg_list):
    if len(arg_list) > 1:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "not" method')
    if not isinstance(arg_list[0], bool):
        sys.exit('\n\nTypeError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', the type of argument passed to "not" method should be boolean')
    return not arg_list[0]


def null_ch(arg_list):
    if len(arg_list) != 1:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "null?" method')
    return arg_list[0] == []


def number_ch(arg_list):
    for i in arg_list:
        if not isinstance(i, int) and not isinstance(i, float):
            return False
    return True


def symbol_ch(arg_list):
    for i in arg_list:
        if not isinstance(i, str):
            return False
    return True


def list_ch(arg_list):
    if len(arg_list) != 1:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "cons" method')
    return isinstance(arg_list[0], list)


def round_f(arg_list):
    if len(arg_list) > 1:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "round" method')
    return round(arg_list[0])


def remainder_f(arg_list):
    if len(arg_list) != 2:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "remainder" method')
    return arg_list[0] % arg_list[1]


def string_append_f(arg_list):
    for i in range(len(arg_list)):
        arg_list[i] = str(arg_list[i])
    string = ' '.join(arg_list)
    return string


def display_f(arg_list):
    if len(arg_list) > 1:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "display" method')
    if isinstance(arg_list[0], list):
        string = '('
        for i in range(len(arg_list[0]) - 1):
            string = string + str(arg_list[0][i]) + ' '
        string = string + str(arg_list[0][-1]) + ')'
        arg_list[0] = string
    if isinstance(arg_list[0], bool):
        if arg_list[0]:
            arg_list[0] = '#t'
        else:
            arg_list[0] = '#f'
    elif isinstance(arg_list[0], float):
        arg_list[0] = float(arg_list[0])
    elif isinstance(arg_list[0], int):
        arg_list[0] = int(arg_list[0])
    elif arg_list[0][0] == '\"':
        arg_list[0] = arg_list[0].strip('\"\"')
    print(arg_list[0], end='')
    return arg_list[0]


def newline_f(arg_list):
    print()
    return '\n'


def if_f(arg_list):
    from interpreter import evaluate
    if len(arg_list) != 3:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ',incorrect number of arguments passed to "if" method')
    if evaluate(arg_list[0]):
        return evaluate(arg_list[1])
    else:
        return evaluate(arg_list[2])


def set_f(arg_list):
    if isinstance(arg_list[0], str):
        if not arg_list[0][0].isdigit():
            var = {arg_list[0]: arg_list[1]}
            identifiers.update(var)
        else:
            sys.exit('\n\nValueError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', a variable should start with a letter, not a digit')
    else:
        sys.exit('\n\nTypeError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', unexpected type given to "set!" method')


def begin_f(arg_list):
    from interpreter import evaluate
    for el in arg_list:
        evaluate(el)


def define_f(arg_list):
    if isinstance(arg_list[0], str):
        if not arg_list[0][0].isdigit():
            var = {arg_list[0]: arg_list[1]}
            identifiers.update(var)
        else:
            sys.exit('\n\nValueError: in line ' +
                     str(getframeinfo(currentframe()).lineno) +
                     ', a variable should start with a letter not a digit')
    elif isinstance(arg_list[0], list):
        dict_list = []
        func_name = arg_list[0][0]
        func_args = arg_list[0][1:]
        func_body = arg_list[1]
        dict_list.append(func_args)
        dict_list.append(func_body)
        func = {func_name: dict_list}
        functions.update(func)
    else:
        sys.exit('\n\nTypeError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', unexpected type given to "define" method')


def lambda_f(arg_list):
    dict_list = []
    arg_list[0] = 'lambda_func'
    func_args = arg_list[1]
    func_body = arg_list[2]
    dict_list.append(func_args)
    dict_list.append(func_body)
    functions.update({arg_list[0]: dict_list})
    return arg_list[0]


def list_f(arg_list):
    return arg_list


def car_f(arg_list):
    return arg_list[0]


def cdr_f(arg_list):
    return arg_list[1:]


def cons_f(arg_list):
    if len(arg_list) != 2:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', incorrect number of arguments passed to "cons" method')
    tmp = []
    for i in arg_list[0]:
        tmp.append(i)
    for i in arg_list[1]:
        tmp.append(i)
    return tmp


def append_f(arg_list):
    return cons_f(arg_list)


def length_f(arg_list):
    return len(arg_list) + 1


identifiers = {}
functions = {}
current_func = {}
dictionary = {
    '+': op_add,
    '-': op_sub,
    '*': op_mul,
    '/': op_truediv,
    '>': op_gt,
    '<': op_lt,
    '>=': op_ge,
    '<=': op_le,
    '=': op_eq,
    'abs': op_abs,
    'begin': begin_f,
    'eq?': eq_ref_ch,
    'equal?': equal_ch,
    'max': max_f,
    'min': min_f,
    'not': not_f,
    'and': and_f,
    'or': or_f,
    'null?': null_ch,
    'number?': number_ch,
    'round': round_f,
    'remainder': remainder_f,
    'symbol?': symbol_ch,
    'display': display_f,
    'newline': newline_f,
    'set!': set_f,
    'string-append': string_append_f,
    'append': append_f,
    'car': car_f,
    'cdr': cdr_f,
    'cons': cons_f,
    'length': length_f,
    'list': list_f,
    'list?': list_ch,
}
