#!/usr/bin/env python3
""" type annotations tasks """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return sum of list of floats """
    result = 0
    for i in input_list:
        result += i
    return result
