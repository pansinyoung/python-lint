"""
115. Unique Paths II
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example
Example 1:
	Input: [[0]]
	Output: 1


Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2

	Explanation:
	Only 2 different path.


Notice
m and n will be at most 100.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i - 1][j] if i - 1 >= 0 else 0) + (obstacleGrid[i][j - 1] if j - 1 >= 0 else 0)
        return obstacleGrid[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]]))
