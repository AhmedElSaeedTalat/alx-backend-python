#!/usr/bin/env python3
""" type annotations tasks """


def sum_list(input_list: [float]) -> float:
    """ return sum of list of floats """
    result = 0
    for i in input_list:
        result += i
    return result
