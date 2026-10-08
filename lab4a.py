#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py
from random import randint as rng

def is_even(ls:list) -> bool:
    """Function accepts a list and returns True if it contains an even number

    Args:
        ls (list): A list of integers

    Returns:
        bool: True if list contains even number; False otherwise.
    """
    for n in ls:
        if n % 2 == 0:
            return True
    return False

test_lists = [
    [i * 2 + 1 for i in range(6)],  # False (Odd numbers)
    [7, 67, 11, 95, 89, 69420],     # True (All odd except the last)
    [rng(1, 999) for _ in range(6)] # Could be True or False
]

padding = max([len(str(x)) for x in test_lists])
for ls in test_lists:
    print(f"{str(ls):<{padding}} | {is_even(ls)}")
