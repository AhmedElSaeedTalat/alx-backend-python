#!/usr/bin/env python3
""" type annotations tasks """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, int]:
    """ function that creates and return tuple """
    vPowered: float = v * v
    newTuple = (k, vPowered)
    return newTuple
