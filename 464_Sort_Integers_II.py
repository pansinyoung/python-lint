"""
464. Sort Integers II
Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example
Example1:

Input: [3, 2, 1, 4, 5],
Output: [1, 2, 3, 4, 5].
Example2:

Input: [2, 3, 1],
Output: [1, 2, 3].
"""


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # result = self.quickSort(A)
        # for i in range(len(A)):
        #     A[i] = result[i]

        self.mergeSort(A, 0, len(A) - 1)

    def quickSort(self, A):
        if not A or len(A) == 1:
            return A
        pivot = A[len(A) // 2]
        upper, equal, lower = [], [], []
        for i in A:
            if i > pivot:
                upper.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                lower.append(i)
        return self.quickSort(lower) + equal + self.quickSort(upper)

    def mergeSort(self, A, start, end):
        if start >= end:
            return
        if start == end - 1:
            if A[start] > A[end]:
                temp = A[end]
                A[end] = A[start]
                A[start] = temp
            return

        mid = (start + end - 1) // 2
        self.mergeSort(A, start, mid)
        self.mergeSort(A, mid + 1, end)

        temp = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if A[i] <= A[j]:
                temp.append(A[i])
                i += 1
            else:
                temp.append(A[j])
                j += 1

        while i <= mid:
            temp.append(A[i])
            i += 1
        while j <= end:
            temp.append(A[j])
            j += 1

        for i in range(len(temp)):
            A[start + i] = temp[i]

def main():
    s = Solution()
    A = [1, 3, 1, 4, 4, 2, 1, 1]
    s.sortIntegers2(A)
    print(A)


if __name__ == '__main__':
    main()
