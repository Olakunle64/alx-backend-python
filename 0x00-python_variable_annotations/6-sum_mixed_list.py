#!/usr/bin/env python3
"""This module has a function named <sum_mixed_list which takes a list
    of integers and floats and return their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list of integers and floats and
        return their sum

        Args:
            mxd_lst: list of integers and floats

        Return: return their sum as a float
    """
    result: float = 0.0
    for num in mxd_lst:
        result += num
    return float(result)
