#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    result = [[1]]  # 1st row is always 1

    # 1st row is already made above
    for i in range(n - 1):
        # temp list, not modifying result list
        temp = [0] + result[-1] + [0]

        row = []
        # building the new row, len of prev row + 1
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)

    return result
