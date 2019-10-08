"""
109. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Example
Example 1:

Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Example 2:

Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
Notice
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        i = len(triangle) - 1
        memo = triangle[i][:]
        while i > 0:
            i -= 1
            for j in range(i + 1):
                memo[j] = triangle[i][j] + min(memo[j], memo[j + 1])
        return memo[0]


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 2],
        [6, 5, 7],
        [4, 4, 8, 1]
    ]
    print(Solution().minimumTotal(triangle))
