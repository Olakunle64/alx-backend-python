#!/usr/bin/env python3
"""This module has a function named <async_comprehension> that takes
    no arguments
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This uses async comprehension to call <async_generator>
        function and return a list of the random numbers generated
    """
    rand_numbers: List[float] = [num async for num in async_generator()]
    return rand_numbers
