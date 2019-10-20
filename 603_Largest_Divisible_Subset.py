"""
603. Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

Example
Example 1:

Input: nums =  [1,2,3],
Output: [1,2] or [1,3]
Example 2:

Input: nums = [1,2,4,8],
Output: [1,2,4,8]
Notice
If there are multiple solutions, return any subset is fine.
"""



class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [[_] for _ in nums]
        max_array = [] if not dp[0] else dp[0]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and len(dp[i]) - 1 < len(dp[j]):
                    dp[i] = [dp[i][0]] + dp[j]
                    max_array = dp[i] if len(dp[i]) > len(max_array) else max_array
        return max_array


print(Solution().largestDivisibleSubset([3,6,9,27,81,22,24,56,243,486,726,18,36,72]))