"""
685. First Unique Number in Data Stream
Given a continuous stream of data, write a function that returns the first unique number (including the terminating number) when the terminating number arrives. If the unique number is not found, return -1.

Example
Example1

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input:
[1, 2, 2, 1, 3, 4]
3
Output: 3
"""


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def helpPrinter(self, dummy, n):
        print('----------', n, '---------')
        cur = dummy
        while cur.next:
            print(cur.next.val)
            cur = cur.next

    def firstUniqueNumber(self, nums, number):
        dummy = LinkedNode(-1)
        unique_map_to_prev = {}
        tail = dummy
        visited = set()
        for n in nums:
            if n not in visited:
                node = LinkedNode(n)
                tail.next = node
                unique_map_to_prev[n] = tail
                tail = tail.next
                visited.add(n)
            elif n in unique_map_to_prev:
                node = unique_map_to_prev[n].next
                if node == tail:
                    tail = unique_map_to_prev[n]
                    tail.next = None
                else:
                    unique_map_to_prev[node.next.val] = unique_map_to_prev[n]
                    unique_map_to_prev[n].next = node.next
                del unique_map_to_prev[n]

            if n == number:
                return dummy.next.val
            # self.helpPrinter(dummy, n)
            # print([unique_map_to_prev[u].val for u in unique_map_to_prev])
        return -1
