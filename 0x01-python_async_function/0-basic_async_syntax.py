#!/usr/bin/env python3
"""This module has a function named wait_random"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This function uses asynchrounous coroutine that
        takes in an integer argument <max_delay> with a
        default value of 10 that waits for a random delay
        between 0 and max_delay and eventually returns it

        Args:
            max_delay: int

        Return:
            return the randomly generated float value.
    """
    num: float = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return (num)
