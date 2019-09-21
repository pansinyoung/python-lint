"""
61. Search for a Range
中文English
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Example 1:

Input:
[]
9
Output:
[-1,-1]

Example 2:

Input:
[5, 7, 7, 8, 8, 10]
8
Output:
[3, 4]
Challenge
O(log n) time.
"""
from typing import List


class Solution:
    def searchRange(self, A: List[int], target: int) -> List[int]:
        if not A:
            return [-1, -1]
        n = len(A)
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] != target and A[end] != target:
            return [-1, -1]
        i = start if A[start] == target else end
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[start] != target and A[end] != target:
            return [-1, -1]
        j = end if A[end] == target else start
        return [i, j] if i <= j else [-1, -1]


def main():
    s = Solution()
    source = []
    target = 0
    print(s.searchRange(source, target))


if __name__ == "__main__":
    main()
