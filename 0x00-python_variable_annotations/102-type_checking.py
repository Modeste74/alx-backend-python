#!/usr/bin/env python3
"""Annotating the function"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Annotation done"""
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
