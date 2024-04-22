#!/usr/bin/env python3
"""
Async routine that spawns task_wait_random n times
"""

from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times task_wait_random will be spawned.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
