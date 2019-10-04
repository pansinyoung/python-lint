"""
533. Two Sum - Closest to target
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the absolute value of difference between the sum of the two integers and the target.

Example
Example1

Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
Example2

Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
Challenge
Do it in O(nlogn) time complexity.
"""
import sys

class Solution:
    def twoSumClosest(self, nums, target):
        if not nums or len(nums) < 2:
            return -1
        nums.sort()
        start, end = 0, len(nums) - 1
        result = sys.maxsize
        while start < end:
            cur_sum = nums[start] + nums[end]
            print(cur_sum)
            result = min(result, abs(target - cur_sum))
            if result == 0:
                break
            if cur_sum < target:
                start += 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
            else:
                end -= 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
        return result


def main():
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 3
    print(s.twoSumClosest(nums, target))


if __name__ == "__main__":
    main()
