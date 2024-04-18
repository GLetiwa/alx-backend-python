#!/usr/bin/env python3
"""type annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums up a floated list"""
    return sum(input_list)
