#!/usr/bin/env python3
"""async generator coroutine"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async waits for a random
    number to yield
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
