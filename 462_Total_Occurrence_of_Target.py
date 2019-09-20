"""
462. Total Occurrence of Target
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Example1:

Input: [1, 3, 3, 4, 5] and target = 3,
Output: 2.
Example2:

Input: [2, 2, 3, 4, 6] and target = 4,
Output: 1.
Example3:

Input: [1, 2, 3, 4, 5] and target = 6,
Output: 0.
Challenge
Time complexity in O(logn)
"""
from typing import List


class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A: List[int], target: int) -> int:
        if not A:
            return 0
        n = len(A)
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] != target and A[end] != target:
            return 0
        else:
            i = start if A[start] == target else end

        start, end = 0, n
        while start < end - 1:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[start] != target and A[end] != target:
            return 0
        else:
            j = start if A[start] == target else end
        if i == j and A[i] != target:
            return 0
        return j - i + 1


def main():
    s = Solution()
    x = [1, 1]
    n = 1

    print(s.totalOccurrence(x, n))


if __name__ == "__main__":
    main()
