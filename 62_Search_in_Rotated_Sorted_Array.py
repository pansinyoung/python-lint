"""
62. Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
Example 1:

Input: [4, 5, 1, 2, 3] and target=1,
Output: 2.
Example 2:

Input: [4, 5, 1, 2, 3] and target=0,
Output: -1.
Challenge
O(logN) time
"""
from typing import List


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A: List[int], target: int) -> int:
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start < end - 1:
            print(start, end)
            mid = (start + end) // 2
            m = A[mid]
            if m == target:
                return mid
            s = A[start]
            e = A[end]
            if s > e:
                if m > target >= s or target >= s > m or e > m > target:
                    end = mid
                else:
                    start = mid
            else:
                if target > m:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1




def main():
    s = Solution()
    test = []
    print(s.search(test, 3))


if __name__ == '__main__':
    main()
