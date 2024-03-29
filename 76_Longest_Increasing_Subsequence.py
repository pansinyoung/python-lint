"""
76. Longest Increasing Subsequence
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Example
Example 1:
	Input:  [5,4,1,2,3]
	Output:  3

	Explanation:
	LIS is [1,2,3]


Example 2:
	Input: [4,2,4,5,3,7]
	Output:  4

	Explanation:
	LIS is [2,4,5,7]
Challenge
Time complexity O(n^2) or O(nlogn)

Clarification
What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""


class Solution:
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        dp = [1 for _ in nums]
        max_count = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] - 1, dp[j]) + 1
            max_count = max(max_count, dp[i])
        return max_count + 1