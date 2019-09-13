"""
433. Number of Islands
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we
consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1
"""
from typing import List


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid: List[List[int]]):
        if not grid:
            return 0
        result, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    if (i - 1 < 0 or grid[i - 1][j] != 2) \
                            and (j - 1 < 0 or grid[i][j - 1] != 2) \
                            and (i + 1 >= m or grid[i + 1][j] != 2) \
                            and (j + 1 >= n or grid[i][j + 1] != 2):
                        if i - 1 >= 0 and grid[i - 1][j] != 0:
                            grid[i - 1][j] = 2
                        if j - 1 >= 0 and grid[i][j - 1] != 0:
                            grid[i][j - 1] = 2
                        if i + 1 < m and grid[i + 1][j] != 0:
                            grid[i + 1][j] = 2
                        if j + 1 < n and grid[i][j + 1] != 0:
                            grid[i][j + 1] = 2
                        result += 1
        return result


    def removeIsland(self, grid: List[List[int]], i: int, j: int):


def main():
    s = Solution()
    test1 = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1]]
    test2 = [[1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]]
    print(test1, s.numIslands(test1))
    print(test2, s.numIslands(test2))


if __name__ == '__main__':
    main()
