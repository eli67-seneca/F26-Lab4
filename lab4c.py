#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

def _sum(x:int, y:int) -> int:
    """Returns the sum of two numbers.

    Args:
        x (int): The addend
        y (int): The augend

    Returns:
        int: The sum
    """
    # return sum([num1, num2])
    return x + y

def main():
    inputs = []
    while len(inputs) < 2:
        n = None
        try:
            n = int(input("Input a number:\n> "))
        except ValueError:
            print("Invalid number!\n")
            pass
        
        inputs.append(n) if n else None

    addend, augend = inputs
    the_sum = _sum(*inputs)
    print(f"{addend} + {augend} = {the_sum}")

if __name__ == "__main__":
    main()