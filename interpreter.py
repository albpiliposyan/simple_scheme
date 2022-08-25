"""
Simple Lisp Interpreter in python

Implemented by Albert Piliposyan

Libraries:
    os, sys, copy, inspect
    parsing, scheme_methods

Versions:
    Python 3.8.*

"""

import parsing
import time
from copy import deepcopy
from scheme_methods import (dictionary, functions, current_func, identifiers,
                            if_f, define_f, set_f, lambda_f)


def replace_arguments(expr, variables, args):
    for i in range(len(expr)):
        if isinstance(expr[i], list):
            replace_arguments(expr[i], variables, args)
        elif isinstance(expr[i], str):
            if expr[i] in args:
                expr[i] = variables[args.index(expr[i])]
        else:
            continue
    return expr


def function_call(expr, index):
    current_func.update(deepcopy(functions))
    variables = expr[1:]
    args = current_func[expr[index]][0]
    body = current_func[expr[index]][1]
    expr = replace_arguments(body, variables, args)
    expr = evaluate(expr)
    current_func.clear()
    return expr


def evaluate(expr):
    # print('CURRENT EXPRESSION:\n' + str(expr))
    if not isinstance(expr, list):
        return expr
    if not expr:
        return expr

    for i in range(len(expr)):
        # print('EXPRESSION\n' + str(expr))
        if not isinstance(expr, list):
            return expr
        if isinstance(expr[i], list):
            if expr[0] == 'if':
                return if_f(expr[1:])
            elif expr[0] == 'define':
                return define_f(expr[1:])
            if expr[0] == 'lambda':
                return lambda_f(expr)
            else:
                expr[i] = evaluate(expr[i])
        elif isinstance(expr[i], str):
            if expr[0] == 'set!':
                return set_f(expr[1:])
            elif expr[0] == 'define':
                return define_f(expr[1:])
            if expr[i] in identifiers:
                expr[i] = identifiers[expr[i]]
            elif expr[i] in functions:
                expr = function_call(expr.copy(), i)

    # print('EDITING EXPRESSION:\n' + str(expr))
    for i in range(len(expr)):
        if isinstance(expr[i], list):
            evaluate(expr[i])
    if isinstance(expr[0], str):
        if expr[0] in dictionary:
            return dictionary[expr[0]](expr[1:])
        elif expr[0] in functions:
            expr = function_call(expr, 0)
    if isinstance(expr, list) and len(expr) == 1:
        return expr[0]
    return expr


def interpret(input_file):
    fi = open(input_file, 'r')
    input_text = fi.read()
    fi.close()
    tokens = parsing.tokenize(input_text)
    parenthesized = parsing.parenthesize(tokens)
    evaluate(parenthesized)


def main():
    input_file = './test.scm'
    interpret(input_file)


if __name__ == "__main__":
    st = time.time()
    main()
    end = time.time()
    print('\n\nEXECUTION TIME: ', end - st)
