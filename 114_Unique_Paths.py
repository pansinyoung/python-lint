"""
114. Unique Paths
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Example
Example 1:

Input: n = 1, m = 3
Output: 1
Explanation: Only one path to target position.
Example 2:

Input:  n = 3, m = 3
Output: 6
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
Notice
m and n will be at most 100.
The answer is guaranteed to be in the range of 32-bit integers
"""


class Solution:
    #  DP
    def uniquePaths(self, m, n):
        memo = [[0 for _ in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]

    # recursion
    # def uniquePaths(self, m, n):
    #     return self.helper(m, n, {})
    #
    # def helper(self, m, n, memo):
    #     if not (m > 1 and n > 1):
    #         return min(m, n)
    #     if (m, n) in memo:
    #         return memo[(m, n)]
    #     cur = self.helper(m - 1, n, memo) + self.helper(m, n - 1, memo)
    #     memo[(m, n)] = cur
    #     return cur


print(Solution().uniquePaths(6, 63))
