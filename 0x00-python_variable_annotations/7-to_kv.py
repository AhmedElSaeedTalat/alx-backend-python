#!/usr/bin/env python3
""" type annotations tasks """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv: function that creates and return tuple """
    return (k, v**2)
