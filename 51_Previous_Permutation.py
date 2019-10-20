"""
51. Previous Permutation
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Example
Example 1:

Input:[1]
Output:[1]
Example 2:

Input:[1,3,2,3]
Output:[1,2,3,3]
Example 3:

Input:[1,2,3,4]
Output:[4,3,2,1]

Notice
The list may contains duplicate integers
"""


class Solution:
    def previousPermuation(self, nums):
        if not nums or len(nums) == 0:
            return []
        n = len(nums)
        if len(nums) == 1:
            return nums
        i = n - 1
        while i > 0:
            if nums[i - 1] > nums[i]:
                break
            i -= 1
        if i == 0:
            return nums[::-1]
        index = i
        for j in range(n - 1, i, -1):
            if nums[index] < nums[j] < nums[i - 1]:
                index = j
            if nums[j] == nums[index]:
                index = max(j, index)
        nums[index], nums[i - 1] = nums[i - 1], nums[index]
        return nums[:i] + nums[:i - 1: -1]


if __name__ == '__main__':
    print(Solution().previousPermuation([4, 4, 2, 4]))
