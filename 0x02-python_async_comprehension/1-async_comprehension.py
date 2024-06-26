#!/usr/bin/env python3
"""async comprehension coroutine"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers
    using async comprehension over
    async generator
    """
    result = [i async for i in async_generator()]
    return result
