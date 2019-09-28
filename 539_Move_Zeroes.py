"""
539. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example
Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
Notice
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        i, j = 0, 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            if i >= len(nums) - 1:
                break
            j = i + 1 if i >= j else j
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j == len(nums):
                break
            nums[i] = nums[j]
            nums[j] = 0
            i += 1


def main():
    s = Solution()
    A = [5, 4, 3, 2, 1]

    print(s.findPeak(A))


if __name__ == '__main__':
    main()
