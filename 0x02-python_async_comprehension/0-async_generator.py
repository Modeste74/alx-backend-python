#!/usr/bin/env python3
"""defines a function asyn_generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Takes no args loops 10 time while awaiting 1
    second and the returns a random number between
    0 and 10"""
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
