"""
242. Convert Binary Tree to Linked Lists by Depth
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Example
Example 1:

Input: {1,2,3,4}
Output: [1->null,2->3->null,4->null]
Explanation:
        1
       / \
      2   3
     /
    4
Example 2:

Input: {1,#,2,3}
Output: [1->null,2->null,3->null]
Explanation:
    1
     \
      2
     /
    3
"""
"""
Definition of TreeNode:
Definition for singly-linked list.
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root: TreeNode) -> List[ListNode]:
        if not root:
            return []
        queue = deque()
        result_queue = deque()
        queue.append('#')
        queue.append(root)
        result = []
        while queue:
            cur = queue.popleft()
            if cur == '#':
                result_queue.append('#')
                if queue:
                    queue.append('#')
            else:
                result_queue.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        cur_list = None
        while result_queue:
            cur = result_queue.popleft()
            if cur == '#':
                if result_queue:
                    cur = result_queue.popleft()
                    cur_list = ListNode(cur)
                    result.append(cur_list)
                    continue
            else:
                new_node = ListNode(cur)
                cur_list.next = new_node
                cur_list = new_node
        return result


def main():
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5

    print(s.binaryTreeToLists(t1))


if __name__ == '__main__':
    main()
