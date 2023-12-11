#!/usr/bin/env python3
"""defines an async function
wait_random"""
import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[float] = 10) -> float:
    """waits for a random delay between
    0 and max_delay second and returns it"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
