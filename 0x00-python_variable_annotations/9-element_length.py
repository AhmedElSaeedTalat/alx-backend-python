#!/usr/bin/env python3
""" type annotations tasks for Sequence and Iterable"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function returns list of tuples """
    return [(i, len(i)) for i in lst]
