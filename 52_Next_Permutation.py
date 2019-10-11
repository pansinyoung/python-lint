"""
52. Next Permutation
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

Example
Example 1:

Input:[1]
Output:[1]
Example 2:

Input:[1,3,2,3]
Output:[1,3,3,2]
Example 3:

Input:[4,3,2,1]
Output:[1,2,3,4]
Notice
The list may contains duplicate integers.
"""


class Solution:
    def nextPermutation(self, nums):
        if not nums or len(nums) <= 0:
            return []
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            return nums[:: -1]
        min_index = i
        for j in range(n - 1, i - 1, -1):
            if nums[i - 1] < nums[j] < nums[min_index]:
                min_index = j
            if nums[j] == nums[min_index]:
                min_index = max(min_index, j)
        nums[i - 1], nums[min_index] = nums[min_index], nums[i - 1]
        return nums[:i] + nums[:i - 1: -1]


if __name__ == '__main__':
    print(Solution().nextPermutation([1, 3, 1]))
