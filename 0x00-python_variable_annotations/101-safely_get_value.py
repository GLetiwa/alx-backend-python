#!/usr/bin/env python3
"""function annotation"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')  # creates a generic type variable


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Returns the value for a given key
    if it exists in the dictionary,
    otherwise returns default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
