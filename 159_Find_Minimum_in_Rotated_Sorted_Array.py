"""
159. Find Minimum in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.
Notice
You can assume no duplicate exists in the array.
"""
from typing import List


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end - 1:
            print(start, end)
            mid = (end + start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])


def main():
    s = Solution()
    x = [1, 2]

    print(s.findMin(x))


if __name__ == "__main__":
    main()
