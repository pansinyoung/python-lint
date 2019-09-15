"""
458. Last Position of Target
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
"""
from typing import List


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        i, j = 0, len(nums)
        result = -1
        while i < j:
            mid_ind = (i + j) // 2
            mid = nums[mid_ind]
            if mid == target:
                result = mid_ind if mid_ind > result else result
            if mid > target:
                j = mid_ind
            else:
                i = mid_ind + 1
        return result


def main():
    s = Solution()
    nums = [1, 2, 2, 4, 5, 5]
    target = 2
    print(s.lastPosition(nums, target))


if __name__ == '__main__':
    main()
