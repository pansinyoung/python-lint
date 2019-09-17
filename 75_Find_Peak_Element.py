"""
75. Find Peak Element
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example
Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6

	Explanation:
	return the index of peek.


Example 2:
	Input: [1,2,3,4,1]
	Output:  3

Challenge
Time complexity O(logN)

Notice
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
"""
from typing import List


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A: List[int]):
        start, end = 0, len(A) - 1
        while start < end - 1:
            mid = (start + end) // 2
            mid_num = A[mid]
            if A[mid - 1] < mid_num and A[mid + 1] < mid_num:
                return mid
            if A[mid - 1] < mid_num:
                start = mid
            else:
                end = mid
        return start if A[start] > A[end] else end


def main():
    s = Solution()
    A = [5, 4, 3, 2, 1]

    print(s.findPeak(A))


if __name__ == '__main__':
    main()
