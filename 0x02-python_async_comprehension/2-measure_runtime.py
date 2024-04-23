#!/usr/bin/env python3
"""four parallel comprehensions"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    executes async_comprehension 4 times
    and measures total execution time
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
