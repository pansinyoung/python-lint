"""
1225. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and
there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside
that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.

Example
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""


class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """

    def islandPerimeter(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        result += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        result += 1
                    if j + 1 >= len(grid[0]) or grid[i][j + 1] == 0:
                        result += 1
                    if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                        result += 1

        return result


def main():
    s = Solution()
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))


if __name__ == '__main__':
    main()
