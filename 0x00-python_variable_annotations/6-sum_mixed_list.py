#!/usr/bin/env python3
""" type annotations tasks """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum int and floats """
    result = 0
    for i in mxd_lst:
        result += i
    return result
