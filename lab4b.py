#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py
from random import randint as rng
from math import pi

def even_numbers(ls:list) -> list:
    """Returns a list of all even numbers in `ls`.
    If empty or no even numbers, returns an empty list.

    Args:
        ls (list): Input list of integers

    Returns:
        list: A list of even numbers, potentially.
    """    
    arr = []    # Create an empty list
    for i in ls:
        if i % 2 == 0:
            arr.append(i)
    # If the input list was empty, `arr` would remain empty.
    # return [n for n in ls if x % 2 == 0]
    return arr

test_lists = [
    [8, 16, 18, 1, 3, 14, 7, 9],                    # List of 8 random numbers chosen by simulated physical d20 roll
    [rng(0, 999) for _ in range(8)],                # List of eight ints chosen by PRNG
    list(map(int, str(pi).replace('.', '')[:8])),   # The first 8 digits of pi
]

padding = max([len(str(x)) for x in test_lists])
for ls in test_lists:
    print(f"{str(ls):<{padding}} | {even_numbers(ls)}")
