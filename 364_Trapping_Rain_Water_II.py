"""
364. Trapping Rain Water II
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.



Example
Example 1:

Given `5*4` matrix
Input:
[[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
Output:
14
Example 2:

Input:
[[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]
Output:
0
"""

import heapq


class Solution():
    def trapRainWater(self, heights):
        if not heights or not heights[0]:
            return 0

        m, n = len(heights), len(heights[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heights[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heights[x][y])
                    heapq.heappush(heap, (max(heights[x][y], height), x, y))
                    visited[x][y] = 1
        return result


if __name__ == '__main__':
    print(Solution().trapRainWater([[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]))
