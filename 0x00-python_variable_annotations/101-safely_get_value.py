#!/usr/bin/python3
"""This module has a function named <safely_get_value>
    that takes in a dictionary, key, and a default value and return
    the value of the key or None
"""
from typing import Mapping, Optional, Union, TypeVar, Any


def safely_get_value(
        dct: Mapping, key: Any, default: Union[TypeVar("T"), None] = None
        ) -> Union[Any, TypeVar("T")]:
    """This function takes in a dict, key, default value and check if
        a key is present in a dictionary and then return the
        value of the key or None if it doesn't

        Args:
            dict: a dictionary
            key: a key
            default: None

        Return: return None or the value that belongs to the key
    """
    if key in dct:
        return dct[key]
    else:
        return default
