#!/usr/bin/env python3
"""Defines a function measure_runtime"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """calls a function async_comprehension
    4 times and calculates the total runtime"""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
