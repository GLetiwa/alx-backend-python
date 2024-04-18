#!/usr/bin/env python3
"""type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        """callable function"""
        return x * multiplier
    return multiplier_function
