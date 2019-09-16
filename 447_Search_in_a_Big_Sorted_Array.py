"""

447. Search in a Big Sorted Array
中文English
Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
Challenge
O(logn) time, n is the first index of the given target number.

Notice
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.
"""
"""
Definition of ArrayReader
"""


class ArrayReader(object):
    def __init__(self, data):
        self.data = data

    def get(self, index):
        if index >= len(self.data):
            return 2**31 - 1
        else:
            return self.data[index]


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        i, j = 0, 1
        while True:
            if reader.get(j) >= target:
                break
            else:
                i = j
                j = 2 * j + 1
        j += 1
        while i < j:
            mid_ind = (i + j) // 2
            mid_num = reader.get(mid_ind)
            if mid_num >= target:
                j = mid_ind
            else:
                i = mid_ind + 1
        return i if reader.get(i) == target else -1


def main():
    s = Solution()
    test = ArrayReader([1, 3, 3, 3, 6, 9, 21])
    target = 122
    print(s.searchBigSortedArray(test, target))


if __name__ == '__main__':
    main()
