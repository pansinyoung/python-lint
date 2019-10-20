"""
116. Jump Game
中文English
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example
Example 1

Input : [2,3,1,1,4]
Output : true
Example 2

Input : [3,2,1,0,4]
Output : false
Notice
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
"""


class Solution:
    def canJump(self, A):
        if not A or len(A) == 0:
            return True
        n = len(A)
        dp = [False] * n
        for i in range(n):
            if A[i] != 0:
                for j in range(i + 1, i + A[i] + 1):
                    dp[j] = True
                    if j == n - 1:
                        return True
        return dp[n-1]
