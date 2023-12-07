#!/usr/bin/env python3
""" a type-annotated function to_kv
that takes a string and an int OR float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and an int or
    an float and return a tuple"""
    squared_element: float = v ** 2
    return (k, squared_element)
