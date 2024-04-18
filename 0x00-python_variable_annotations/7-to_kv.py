#!/usr/bin/env python3
"""This module has a function named <to_kv> that takes a string k and
    an int or a float v and return a tuple containing the two args
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes two arguments and use the two arguments
        to form a tuple
    """
    return (k, v ** 2)
