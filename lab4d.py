#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py
from typing import Literal 

def compute(num1:int, num2:int, op:Literal['+', '-', '*', '/']='+') -> int | float | None:
    """Four-function calculator.

    Args:
        num1 (int): The first number
        num2 (int): The second number.
        op (str, optional): Mathematical operator. Defaults to '+'.

    Returns:
        int | float | None: The output. Can be None for divide-by-zero errors.
    """
    output = None
    if op == '+':
        output = num1 + num2
    elif op == '-':
        output = num1 - num2
    elif op == '*':
        output = num1 * num2
    elif op == '/' and num2 != 0:
        output = num1 / num2
    return output

def main():
    """Main function."""
    op = None
    inputs = []
    adverb = ["first", "second"]
    while len(inputs) < 2:
        x = None
        try:
            x = int(input(f"Input {adverb[len(inputs)]} number:\n> "))
        except ValueError:
            print("Invalid input!\n")
            pass
        inputs.append(x) if x else None

    while not op:
        op = input(f"Input operator (+, -, *, /):\n> ")
        if op not in ['+', '-', '*', '/', 'run_test']:
            op = '+'    # Use default operator

    num1, num2 = inputs
    if op != 'run_test':
        print(f"{num1} {op} {num2} = {compute(num1, num2, op)}")
    else:
        test(num1, num2)

def test(num1=13, num2=45):
    """Runs tests"""
    print(compute(num1, num2, '*'))    # 585
    print(compute(num1, num2, '/'))    # 0.2888888888888888886
    print(compute(num1, num2, '-'))    # -32
    print(compute(num1, num2, '+'))    # 58
    print(compute(num1, num2))         # 58

if __name__ == "__main__":
    main()