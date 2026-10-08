#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-07
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

def get_initials(*args) -> list[str]:
    """Returns the first character of all arguments, which are preemptively cast
    into strings.

    Returns:
        list[str]: A list of strings containing the first character of all arguments, if any.
    """
    # Why write many line when one line do trick
    return [str(x[0]) for x in args]

def main():
    """Main function."""
    test_names = ["Alice", "Bob", "Charlie", "David"]
    initials = get_initials(*test_names)    # Unpack operator.
    print(initials)

if __name__ == "__main__":
    main()
