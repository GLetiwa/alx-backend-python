#!/usr/bin/env python3
"""async generator coroutine"""

import asyncio
import random


async def async_generator():
    """
    async waits for a random
    number to yield
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
