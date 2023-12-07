#!/usr/bin/env python3
"""Annotates using TypeVar"""
from typing import TypeVar, Any, Union, Mapping

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """gets the value from a dictionary
    based on the provided key, he value associated
    with the key if found, otherwise
    returns the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
