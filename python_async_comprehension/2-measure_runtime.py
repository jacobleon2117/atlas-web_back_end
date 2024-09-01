#!/usr/bin/env python3
"""
Provides a coroutine to measure the runtime of async_comprehension.

Contains:
    measure_runtime: Coroutine to execute async_comprehension four times in parallel
    and measure the total runtime.
"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to execute async_comprehension four times in parallel using asyncio.gather
    and measure the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time
