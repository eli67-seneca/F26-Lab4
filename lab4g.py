#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

numbers = range(2, 11)
print(f"Numbers:\t\t{list(numbers)}")

squared = map(lambda x: x**2, numbers)
print(f"Squared numbers:\t{list(squared)}")

divisible_by_2 = filter(lambda x: x % 2 == 0, numbers)
print(f"Divisble by two:\t{list(divisible_by_2)}")