#!/usr/bin/env python3
"""Annotating a function element_length"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes list of strings and returns
    a list of tuples"""
    return [(i, len(i)) for i in lst]
