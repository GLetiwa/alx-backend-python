#!/usr/bin/env python3
"""
Measure the runtime of wait_n coroutine
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): Number of times wait_random will be spawned.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Average time taken for each call to wait_random.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
