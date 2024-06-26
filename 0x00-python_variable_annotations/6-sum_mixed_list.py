#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of a mixed list(ints & floats)"""
    return sum(mxd_lst)
