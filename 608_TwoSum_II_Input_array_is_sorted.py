"""
608. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 9
Output: [1, 2]
Example 2:

Input: nums = [2,3], target = 5
Output: [1, 2]
Notice
You may assume that each input would have exactly one solution.
"""
from typing import List
from collections import deque


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            cur = nums[i] + nums[j]
            if cur == target:
                return [i + 1, j + 1]
            if cur > target:
                j -= 1
            else:
                i += 1
        return []


def main():
    s = Solution()
    source = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 1]]
    print(s.zombie(source))


if __name__ == '__main__':
    main()
