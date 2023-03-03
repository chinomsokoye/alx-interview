#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """ Returns perimeter of an island description in grid """
    perimeter = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    a, b = i + x, j + y
                    # print(a, b)
                    if a >= m or b >= n or a < 0 or b < 0 or grid[a][b] == 0:
                        perimeter += 1
    return perimeter
