#!/usr/bin/env python3

"""
Measures the execution time of the wait_n function.

Contains:
    measure_time: Function to measure the average time for wait_n execution.
"""

import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken to execute wait_n.

    Args:
        n (int): Number of delays to generate.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: Average time per execution in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
