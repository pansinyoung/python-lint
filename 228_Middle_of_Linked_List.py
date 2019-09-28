"""
228. Middle of Linked List
Find the middle node of a linked list.

Example
Example 1:

Input:  1->2->3
Output: 2
Explanation: return the value of the middle node.
Example 2:

Input:  1->2
Output: 1
Explanation: If the length of list is  even return the value of center left one.
Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?
"""

"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head: ListNode) -> ListNode:
        tail = head
        while tail:
            if not tail.next:
                return head
            tail = tail.next.next
            if not tail:
                return head
            head = head.next
        return head



def main():
    s = Solution()
    # test = ArrayReader([1, 3, 3, 3, 6, 9, 21])
    # target = 122
    # print(s.searchBigSortedArray(test, target))

if __name__ == '__main__':
    main()
