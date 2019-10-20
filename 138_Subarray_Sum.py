"""
138. Subarray Sum
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]
Notice
There is at least one subarray that it's sum equals to zero.
"""


class Solution:
    def subarraySum(self, nums):
        n = len(nums)
        sum = 0
        dict = {}
        for i in range(n):
            sum += nums[i]
            if sum == 0:
                return [0, i]
            if sum in dict:
                return [dict[sum] + 1, i]
            dict[sum] = i
