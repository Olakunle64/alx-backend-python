#!/usr/bin/env python3
"""This module has a function named <sum_list> which takes a list
    of floats and return their sum as a float

    Args:
        input_list: a list of floats

    Return: return the sum of all floats in the list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function takes in a list of float and return
        the addition of all elements in the list

        Args:
            input_list: a list of float

        Return: return the sum of all elements in the list
    """
    result: float = 0.0
    for num in input_list:
        result += num
    return result
