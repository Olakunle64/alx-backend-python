#!/usr/bin/env python3
"""This module has a function named <task_wait_n>"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function takes in two args and spawn the
        <wait_random> function n times with max_delay and
        return the list of of all values
    """
    values = []
    for _ in range(n):
        task = await task_wait_random(max_delay)
        values.append(task)
    return values
