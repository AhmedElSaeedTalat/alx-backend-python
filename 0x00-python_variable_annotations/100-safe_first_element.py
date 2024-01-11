#!/usr/bin/env python3
""" type annotations tasks """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function receives list and returns first index
    or None"""
    if lst:
        return lst[0]
    else:
        return None
