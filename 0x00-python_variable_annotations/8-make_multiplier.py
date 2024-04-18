#!/usr/bin/python3
"""This module has a function that takes in a float and return
    a function that multiply a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes in a float and return a callback function

        Args:
            multiplier: a float

        Return: return a callback function

        Callback: takes in a float and return the muliplication of
        the parent arg and its arg
    """
    def inner_multiplier(sub_multiplier: float) -> float:
        """inner multiplier"""
        return multiplier * sub_multiplier
    return inner_multiplier
