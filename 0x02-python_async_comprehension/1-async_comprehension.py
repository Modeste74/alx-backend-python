#!/usr/bin/env python3
"""Defines a function async_comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """calls a function async_generator and
    return  a list from the function called"""
    result = [i async for i in async_generator()]
    return result
