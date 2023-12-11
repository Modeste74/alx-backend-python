#!/usr/bin/env python3
"""defines an async function
measure_time"""
import asyncio
import time
from typing import Callable, List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time per call for wait_n function"""
    total_time = 0
    for _ in range(n):
        start_time = time.time()
        asyncio.run(wait_n(n, max_delay))
        end_time = time.time()
        total_time += end_time - start_time

    return total_time / n if n > 0 else 0.0
