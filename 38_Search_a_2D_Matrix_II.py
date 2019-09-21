"""
38. Search a 2D Matrix II
中文English
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
Example
Example 1:

Input:
	[[3,4]]
	target=3
Output:1
Example 2:

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2
Challenge
O(m+n) time and O(1) extra space
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        result = 0
        point = (m - 1, 0)
        while point[0] >= 0 and point[1] < n:
            x, y = point
            if matrix[x][y] == target:
                result += 1
                point = (x - 1, y + 1)
            elif matrix[x][y] > target:
                point = (x - 1, y)
            else:
                point = (x, y + 1)
        return result


def main():
    s = Solution()
    source = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 1
    print(s.searchMatrix(source, target))


if __name__ == "__main__":
    main()
