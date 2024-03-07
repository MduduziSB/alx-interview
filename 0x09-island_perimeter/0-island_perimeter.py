#!/usr/bin/python3
"""
This a program on obtaining the grid of an island.
"""

def island_perimeter(grid):
    """
    This function obtains the grid of an island.

    args:
        grid -> list of list

    return:
        grid perimeter
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
