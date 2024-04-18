#!/usr/bin/env python3
"""mypy fix"""
from typing import Tuple, List


def zoom_array(lst: List[int], factor: int = 2) -> Tuple[int, ...]:
    """mypy code fix"""
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
