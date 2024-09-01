#!/usr/bin/env python3

"""
Provides an async function to spawn multiple random delays.

Contains:
    wait_n: Async function to generate n random delays.
"""


import asyncio
import random
from typing import List 
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    async def add_delay():
        delay = await wait_random(max_delay)
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                return
        delays.append(delay)

    await asyncio.gather(*(add_delay() for _ in range(n)))
    return delays
