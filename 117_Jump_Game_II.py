"""
117. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example
Example 1

Input : [2,3,1,1,4]
Output : 2
Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""


class Solution:
    def jump(self, A):
        if len(A) == 1:
            return 0
        n, dp = len(A), [0 for _ in A]
        for i in range(n-2, -1, -1):
            if A[i] + i >= n - 1:
                dp[i] = 1
            elif A[i] != 0:
                dp[i] = min([dp[j + i] for j in range(1, A[i] + 1) if A[i + j] != 0] or [0]) + 1
        return dp[0]
