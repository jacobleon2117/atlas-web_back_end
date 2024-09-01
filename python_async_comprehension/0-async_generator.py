#!/usr/bin/env python3

"""
Provides an asynchronous generator to yield random numbers.

Contains:
    async_generator: Coroutine to yield random numbers with a 1-second delay.
"""

import asyncio
import random

async def async_generator():
    """
    Asynchronous generator that yields random numbers between 0 and 10
    with a 1-second delay between each yield.

    Yields:
        int: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10) 
