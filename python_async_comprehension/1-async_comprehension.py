#!/usr/bin/env python3
"""
Provides a coroutine to collect numbers using asynchronous comprehension.

Contains:
    async_comprehension: Coroutine to collect 10 random numbers.
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using asynchronous comprehension.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [number async for number in async_generator()]
