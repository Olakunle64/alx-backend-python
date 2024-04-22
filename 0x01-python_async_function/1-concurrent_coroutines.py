#!/usr/bin/env python3
"""This module has a function named <wait_n>"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function takes in two args and spawn the
        <wait_random> function n times with max_delay and
        return the list of of all values
    """
    values = []
    for _ in range(n):
        value = await wait_random(max_delay)
        values.append(value)
    return sorted(values)
