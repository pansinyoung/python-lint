"""
609. Two Sum - Less than or equal to target
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 24.
Output: 5.
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
Example 2:

Input: nums = [1], target = 1.
Output: 0.
"""


class TwoSum:
    def twoSum5(self, nums, target):
        nums.sort()
        result = 0
        for start in range(len(nums) - 1):
            end = len(nums) - 1
            while end > start and nums[start] + nums[end] > target:
                end -= 1
            if end > start:
                result += end - start
        return result


def main():
    s = TwoSum()
    nums = [2, 7, 11, 15]
    target = 24
    print(s.twoSum5(nums, target))


if __name__ == "__main__":
    main()
