"""
460. Find K Closest Elements
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to
target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending
order by number if the difference is same.

Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time

Notice
The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array will not exceed 10^4
​​
"""
from typing import List


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A: List[int], target: int, k: int) -> List[int]:
        m = len(A)
        i, j = 0, m
        closest_ind = -1
        while i < j:
            mid_ind = (i + j) // 2
            mid_num = A[mid_ind]
            if mid_num == target:
                closest_ind = mid_ind
                break
            elif mid_num < target:
                i = mid_ind + 1
            else:
                j = mid_ind
            if closest_ind == -1 or abs(mid_num - target) < abs(A[closest_ind] - target):
                closest_ind = mid_ind
            elif abs(mid_num - target) == abs(A[closest_ind] - target):
                closest_ind = min(mid_ind, closest_ind)

        start = closest_ind
        result = [A[start]]
        i = k - 1
        end = start
        while end + 1 < m and i > 0 and abs(A[end + 1] - target) == abs(A[end] - target):
            result.append(A[end + 1])
            end += 1
            i -= 1
        j = 1
        while i > 0:
            if start - j >= 0:
                result.append(A[start - j])
                i -= 1

            if end + j < m:
                result.append(A[end + j])
                i -= 1
            j += 1
        return result


def main():
    s = Solution()
    A = [1, 4, 6, 8]
    target = 3
    k = 3
    print(s.kClosestNumbers(A, target, k))


if __name__ == '__main__':
    main()
