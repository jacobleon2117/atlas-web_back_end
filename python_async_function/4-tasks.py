#!/usr/bin/env python3
"""
Provides a function to spawn multiple tasks for random delays.

Contains:
    task_wait_n: Function to generate n random delays using tasks.
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for each task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []

    async def gather_delays():
        nonlocal delays
        tasks = [task_wait_random(max_delay) for _ in range(n)]
        completed, _ = await asyncio.wait(tasks)
        for task in completed:
            delays.append(await task)

        delays.sort()

    asyncio.run(gather_delays())
    return delays
