import sys
from inspect import currentframe, getframeinfo


def tokenize(input_file):
    current = 0
    tokens = []
    parens = 0
    while current < len(input_file):
        char = input_file[current]
        if char.isspace():
            current = current + 1
            continue
        elif char == ';':
            while char != '\n':
                current = current + 1
                char = input_file[current]
                continue
            current = current + 1
            continue
        elif char == '(':
            tokens.append('(')
            current = current + 1
            parens = parens + 1
            continue
        elif char == ')':
            tokens.append(')')
            current = current + 1
            parens = parens - 1
            continue
        elif char == '\"':
            value = '\"'
            current = current + 1
            char = input_file[current]
            while char != '\"':
                value += char
                current = current + 1
                char = input_file[current]
            value += '\"'
            current = current + 1
            tokens.append(value)
            continue
        else:
            value = ''
            while char != '(' and char != ')' and not char.isspace():
                value += char
                current = current + 1
                char = input_file[current]
            tokens.append(value)
            continue
    if parens > 0:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', missing a close parenthesis')
    if parens < 0:
        sys.exit('\n\nValueError: in line ' +
                 str(getframeinfo(currentframe()).lineno) +
                 ', unexpected opened parenthesis')
    for i in range(len(tokens)):
        tokens[i] = convert(tokens[i])
    return tokens


def convert(token: str):
    try:
        token = int(token)
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            if token == '#f':
                return bool(False)
            elif token == '#t':
                return bool(True)
            else:
                return str(token)


def parenthesize(tokenized_list):
    index = -1
    for i in range(len(tokenized_list)):
        if tokenized_list[i] == '(':
            index = i
        elif tokenized_list[i] == ')':
            if index == -1:
                break
            inserted_list = tokenized_list[index + 1: i]
            del tokenized_list[index: i + 1]
            tokenized_list.insert(index, inserted_list)
            return parenthesize(tokenized_list)
    return tokenized_list
