#!/usr/bin/env python3
"""
Provides a function to create an asyncio Task for wait_random.

Contains:
    task_wait_random: Function to create and return an asyncio Task.
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The task representing the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
