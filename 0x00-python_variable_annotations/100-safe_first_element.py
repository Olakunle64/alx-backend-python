#!/usr/bin/env python3
"""This module has a function named <safe_first_element that takes
    in a list containing any element and return
    any element or None
"""
from typing import Any, Sequence, Iterable, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function takes in a list of any elements

        Args:
            1st: a list of any elements

        Return: return any element or None
    """
    if lst:
        return lst[0]
    else:
        return None
