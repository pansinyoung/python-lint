"""
459. Closest Number in Sorted Array
Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

Example
Example 1:

Input: [1, 2, 3] , target = 2
Output: 1.
Example 2:

Input: [1, 4, 6], target = 3
Output: 1.
Example 3:

Input: [1, 4, 6], target = 5,
Output: 1 or 2.
Challenge
O(logn) time complexity.

Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.
"""
from typing import List


class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def closestNumber(self, A: List[int], target: int) -> int:
        if not A:
            return -1
        n = len(A)
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid
            else:
                end = mid
        return start if abs(A[start] - target) <= abs(A[end] - target) else end


def main():
    s = Solution()
    x = [1, 4, 6]
    n = 5

    print(s.closestNumber(x, n))


if __name__ == "__main__":
    main()
