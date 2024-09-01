#!/usr/bin/env python3
"""
Asyncio utilities for creating asynchronous coroutines.

This module contains utility functions for creating asynchronous coroutines.
"""
import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (float): Maximum delay in seconds (default: 10.0)

    Returns:
        float: The actual delay waited for in seconds

    Raises:
        ValueError: If max_delay is negative
    """

    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
