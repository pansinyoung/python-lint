"""
190. Next Permutation II
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

Example
Example 1:

Input:1,2,3
Output:1,3,2
Example 2:

Input:3,2,1
Output:1,2,3
Example 3:

Input:1,1,5
Output:1,5,1
Challenge
The replacement must be in-place, do not allocate extra memory.
"""


class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            self.in_place_reverse(nums, 0, n - 1)
        else:
            j = i
            min_num = nums[j]
            min_index = j
            while j < n:
                if nums[i - 1] < nums[j] < min_num:
                    min_num = nums[j]
                    min_index = j
                j += 1
            nums[i - 1], nums[min_index] = nums[min_index], nums[i - 1]
            self.in_place_reverse(nums, i, n - 1)

    def in_place_reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = [1, 2, 3, 4]
    Solution().nextPermutation(nums)
    while nums != result:
        print(nums)
        Solution().nextPermutation(nums)
