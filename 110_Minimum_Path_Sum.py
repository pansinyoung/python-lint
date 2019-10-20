"""
110. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Example
Example 1:
	Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7

	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1


Example 2:
	Input:  [[1,3,2]]
	Output: 6

	Explanation:
	Path is: 1 -> 3 -> 2

Notice
You can only go right or down in the path..
"""


class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        memo = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if i == 0 and j == 0:
                    memo[i][j] = cur
                elif i == 0:
                    memo[i][j] = cur + memo[i][j - 1]
                elif j == 0:
                    memo[i][j] = cur + memo[i - 1][j]
                else:
                    memo[i][j] = cur + min(memo[i - 1][j], memo[i][j - 1])
        return memo[m-1][n-1]


print(Solution().minPathSum([[1,3,2]]))