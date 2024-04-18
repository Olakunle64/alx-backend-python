#!/usr/bin/env python3
"""This module has a function that takes a string and return a list
    of tuple
"""
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function takes an iterable and return a list
        contaning a tuple of each element of the iterable and
        the length

        Args:
            1st: an iterable

        Return: return a list of tuple
    """
    return [(i, len(i)) for i in lst]
