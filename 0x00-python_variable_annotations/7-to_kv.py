#!/usr/bin/env python3
"""type annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts args to a tuple"""
    return (k, v * v)
