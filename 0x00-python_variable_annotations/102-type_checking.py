#!/usr/bin/python3
"""This module has a function named """
from typing import Tuple, Sequence, Any, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A zoom array function"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
