"""
606. Kth Largest Element II
中文English
Find K-th largest element in an array. and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example
Example 1:

Input:[9,3,2,4,8],3
Output:4

Example 2:

Input:[1,2,3,4,5,6,8,9,10,7],10
Output:1

Notice
You can swap elements in the array
"""


import heapq


class Solution:
    def kthLargestElement2(self, nums, k):
        result = []
        for n in nums:
            if len(result) == k:
                heapq.heappushpop(result, n)
            else:
                heapq.heappush(result, n)
        return heapq.heappop(result)
