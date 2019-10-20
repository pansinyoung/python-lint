"""
839. Merge Two Sorted Interval Lists
Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

Example
Example1

Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
Output: [(1,4),(5,6)]
Explanation:
(1,2),(2,3),(3,4) --> (1,4)
(5,6) --> (5,6)
Example2

Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
Output: [(1,2),(3,5),(6,7)]
Explanation:
(1,2) --> (1,2)
(3,4),(4,5) --> (3,5)
(6,7) --> (6,7)
Notice
The intervals in the given list do not overlap.
The intervals in different lists may overlap.
"""
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def mergeTwoInterval(self, list1, list2):
        if not list1 and not list2:
            return []
        i1, i2, n1, n2, next_element, res = 0, 0, len(list1) if list1 else 0, len(list2) if list2 else 0, None, []
        while i1 < n1 or i2 < n2:
            if i1 >= n1 or (i2 < n2 and (list2[i2].start, list2[i2].end) < (list1[i1].start, list1[i1].end)):
                cur = list2[i2]
                i2 += 1
            else:
                cur = list1[i1]
                i1 += 1
            if not next_element:
                next_element = Interval(cur.start, cur.end)
            elif next_element.end < cur.start:
                res.append(next_element)
                next_element = Interval(cur.start, cur.end)
            else:
                next_element.end = max(next_element.end, cur.end)

        return res
