#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times
"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times wait_random will be spawned.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays (float values) in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
