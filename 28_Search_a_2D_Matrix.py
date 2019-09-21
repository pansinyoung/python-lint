"""
28. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Example 1:
    Input:  [[5]],2
    Output: false

    Explanation:
	    false if not included.

Example 2:
    Input: [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ],3
    Output: true

	Explanation:
	return true if included.
Challenge
O(log(n) + log(m)) time
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m - 1
        while start < end - 1:
            mid = (start + end) // 2
            if matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid
        x = start if matrix[end][0] > target else end
        if matrix[x][0] > target or matrix[x][n - 1] < target:
            return False
        start, end = 0, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if matrix[x][mid] > target:
                end = mid - 1
            else:
                start = mid
        if matrix[x][start] == target or matrix[x][end] == target:
            return True
        return False


def main():
    s = Solution()
    source = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 0
    print(s.searchMatrix(source, target))


if __name__ == "__main__":
    main()
