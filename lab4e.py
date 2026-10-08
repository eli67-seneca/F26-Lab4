#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py
def compute(**kwargs) -> int | float | None:
    output = None
    num1 = kwargs.get('num1', 13)
    num2 = kwargs.get('num2', 45)
    op = kwargs.get('op', '+')

    if op == '+':
        output = num1 + num2
    elif op == '-':
        output = num1 - num2
    elif op == '*':
        output = num1 * num2
    elif op == '/' and num2 != 0:
        output = num1 / num2
    return output

def main() -> None:
    """Main function."""
    op = None
    inputs = []
    prompts = ["Input the first number",
               "Input the second number",
               "Input operator (+, -, *, /)"]
    while len(inputs) < 2:
        x = None
        try:
            x = int(input(f"{prompts[len(inputs)]}:\n> "))
        except ValueError:
            print("Invalid input!\n")
            pass
        inputs.append(x) if x else None

    while not op:
        op = input(f"{prompts[len(inputs)]}:\n> ")
        if op not in ['+', '-', '*', '/', 'run_test']:
            op = '+'    # Use default operator

    num1, num2 = inputs
    if op != 'run_test':
        print(f"{num1} {op} {num2} = {compute(num1=num1, num2=num2, op=op)}")
    else:
        test(num1, num2)

def test(num1=13, num2=45) -> None:
    """Runs tests"""
    print(compute(num1=num1, num2=num2, op='*'))    # 585
    print(compute(num1=num1, num2=num2, op= '/'))    # 0.2888888888888888886
    print(compute(num1=num1, num2=num2, op='-'))    # -32
    print(compute(num1=num1, num2=num2, op='+'))    # 58
    print(compute(num1=num1, num2=num2))         # 58

if __name__ == "__main__":
    main()