#!/usr/bin/env python3
"""This module has a function named async_generator that takes
    no arguments
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
        Asynchronous generator that yields random floating-point
        numbers between 1 and 10.

        Yields:
            float: A random floating-point number between 1 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
