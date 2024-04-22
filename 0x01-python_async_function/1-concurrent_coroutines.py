#!/usr/bin/env python3
"""This module has a function named <wait_n>"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> list:
    """This function takes in two args and spawn the
        <wait_random> function n times with max_delay and
        return the list of of all values
    """
    # value = asyncio.gather(wait_random(max_delay), wait_random(max_delay), wait_random(max_delay))
    # values = await value
    # print(values)
    # tasks = [wait_random(max_delay) for _ in range(n)]
    # done, _ = await asyncio.wait(tasks)
    # return [task.result() for task in done]
    values = []
    for _ in range(n):
        value = await wait_random(max_delay)
        print(f'I am ready {value}')
        values.append(value)
    return values