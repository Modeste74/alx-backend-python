#!/usr/bin/env python3
"""defines a type-annotated
function sum_mixed_list"""
from typing import List, Union

mixed_list = List[Union[int, float]]


def sum_mixed_list(mxd_lst: mixed_list) -> float:
    """takes a list of int and
    float and returns a float sum of list"""
    return sum(mxd_lst)
