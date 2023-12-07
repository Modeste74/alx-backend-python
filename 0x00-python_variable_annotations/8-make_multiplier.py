#!/usr/bin/env python3
"""defines a type-annotated function
make_multiplier that takes a
float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier and returns
    a function that multiplies a float
    with multiplier"""

    def multiply_function(value: float) -> float:
        """returned function that multiplier
        gets multiplied with a passed value"""
        return (value * multiplier)
    return (multiply_function)
