"""
585. Maximum Number in Mountain Sequence
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7],
Output: 10
"""
from typing import List


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def mountainSequence(self, nums: List[int]) -> int:
        if not nums:
            return -1
        i, j = 0, len(nums)
        while i < j:
            mid_ind = (i + j) // 2
            if mid_ind == 0 or mid_ind == len(nums) - 1\
                    or (nums[mid_ind] > nums[mid_ind - 1] and nums[mid_ind] > nums[mid_ind + 1]):
                return nums[mid_ind]
            if nums[mid_ind - 1] > nums[mid_ind]:
                j = mid_ind
            else:
                i = mid_ind + 1


def main():
    s = Solution()
    nums = [60]
    print(s.mountainSequence(nums))


if __name__ == '__main__':
    main()
