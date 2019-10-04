"""
587. Two Sum - Unique pairs
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example
Example 1:

Input: nums = [1,1,2,45,46,46], target = 47
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1,1], target = 2
Output: 1
Explanation:
1 + 1 = 2
"""


class Solution:
    def twoSum6(self, nums, target):
        nums.sort()
        result, start, end = 0, 0, len(nums) - 1
        while start < end:
            while end > start and nums[end] + nums[start] > target:
                end -= 1
            if end > start and nums[end] + nums[start] == target:
                result += 1
            start += 1
            while start < len(nums) - 1 and nums[start] == nums[start - 1]:
                start += 1
        return result


def main():
    s = Solution()
    nums = [1,1,2,45,46,46]
    target = 3
    print(s.twoSum6(nums, target))


if __name__ == "__main__":
    main()
