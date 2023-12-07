#!/usr/bin/env python3
"""Annotating safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """takes a sequence of any type and
    returns the type passed or none"""
    if lst:
        return lst[0]
    else:
        return None
