"""
104. Merge K Sorted Lists
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Example
Example 1:
	Input:   [2->4->null,null,-1->null]
	Output:  -1->2->4->null

Example 2:
	Input: [2->6->null,5->null,7->null]
	Output:  2->5->6->7->null
"""

"""
Definition of ListNode
"""
import heapq


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        heap = []
        k = len(lists)
        dummy = ListNode(0, None)
        cur = dummy
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while lists != [None] * k or heap:
            n = heapq.heappop(heap)
            cur.next = ListNode(n[0])
            cur = cur.next
            if lists[n[1]]:
                heapq.heappush(heap, (lists[n[1]].val, n[1]))
                lists[n[1]] = lists[n[1]].next
        return dummy.next
