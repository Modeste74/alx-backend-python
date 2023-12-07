#!/usr/bin/env python3
"""defines a type-annotated
function sum_list"""
from typing import List

float_list = List[float]


def sum_list(input_list: float_list) -> float:
    """returns sum of float list"""
    return sum(input_list)
