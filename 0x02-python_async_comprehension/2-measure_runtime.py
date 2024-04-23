#!/usr/bin/env python3
"""This module has a function named <measure_runtime>"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measure the runtime when <async_comprehension>
        is called four times parallel
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
        )
    return time.perf_counter() - start_time
