"""
130. Heapify
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Example
Example 1

Input : [3,2,1,4,5]
Output : [1,2,3,4,5]
Explanation : return any one of the legitimate heap arrays
Challenge
O(n) time complexity

Clarification
What is heap? What is heapify? What if there is a lot of solutions?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
Return any of them.
"""



class Solution:
    def heapify(self, A):
        n = len(A)
        for i in range(n // 2, -1, -1):
            self.sift_up(A, i)

    def sift_up(self, A, index):
        n = len(A)
        while index < n:
            min_ind = index
            left = index * 2 + 1
            right = index * 2 + 2
            if left < n and A[left] < A[min_ind]:
                min_ind = left
            if right < n and A[right] < A[min_ind]:
                min_ind = right
            if min_ind == index:
                break

            A[index], A[min_ind] = A[min_ind], A[index]
            index = min_ind