#!/usr/bin/python3
"""pascals triangle"""


def print_triangle(n):
    """pascals triangle"""

    if n <= 0:
        return []
    
    previous = [0, 1, 0]
    
    for _ in range(n - 1):
        x = 0
        current = []

        while x + 1  < len(previous):
            current.append(previous[x] + previous[x+1])
            x += 1

        previous = current
        previous.insert(0, 0)
        previous.append(0)

    return previous[1:-1]
