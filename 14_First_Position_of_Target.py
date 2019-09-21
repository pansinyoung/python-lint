"""
14. First Position of Target
中文English
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
Example 1:
Input:  [1,4,4,5,7,7,8,9,9,10]，1
Output: 0

Explanation:
the first index of  1 is 0.

Example 2:
Input: [1, 2, 3, 3, 4, 5, 10]，3
Output: 2

Explanation:
the first index of 3 is 2.

Example 3:
Input: [1, 2, 3, 3, 4, 5, 10]，6
Output: -1

Explanation:
Not exist 6 in array.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
"""

from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] != target and nums[end] != target:
            return -1
        return start if nums[start] == target else end


def main():
    s = Solution()
    source = [1, 4, 4, 5, 7, 7, 8, 9, 9, 10]
    target = 8
    print(s.binarySearch(source, target))


if __name__ == "__main__":
    main()
