"""
443. Two Sum - Greater than target
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Example
Example 1:

Input: [2, 7, 11, 15], target = 24
Output: 1
Explanation: 11 + 15 is the only pair.
Example 2:

Input: [1, 1, 1, 1], target = 1
Output: 6
Challenge
Do it in O(1) extra space and O(nlogn) time.
"""


class TwoSum:
    def twoSum2(self, nums, target):
        nums.sort()
        result, start, end = 0, 0, len(nums) - 1
        while end > start:
            while nums[start] + nums[end] <= target:
                start += 1
            if start < end:
                result += end - start
            end -= 1
        return result


def main():
    s = TwoSum()
    nums = [2, 7, 11, 15]
    target = 24
    print(s.twoSum5(nums, target))


if __name__ == "__main__":
    main()
