#!/usr/bin/env python3
"""
Regular function syntax to create an asyncio.Task
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
