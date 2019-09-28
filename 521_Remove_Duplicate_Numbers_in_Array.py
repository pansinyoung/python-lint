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

    def deduplication(self, nums):
        seen = set()
        i, j = 0, 0
        while i < len(nums):
            while i < len(nums) and nums[i] not in seen and nums[i] is not None:
                seen.add(nums[i])
                i += 1
            if i == len(nums):
                break
            if i == len(nums) - 1 or j == len(nums):
                nums[i] = None
                break
            j = i + 1 if i >= j else j
            while j < len(nums):
                if nums[j] in seen:
                    nums[j] = None
                    j += 1
                else:
                    nums[i] = nums[j]
                    nums[j] = None
                    seen.add(nums[i])
                    j += 1
                    break
            i += 1
        return len(seen)


def main():
    s = Solution()
    A = [1, 3, 1, 4, 4, 2, 1, 1, 1]
    print(s.deduplication(A))
    print(A)


if __name__ == '__main__':
    main()
