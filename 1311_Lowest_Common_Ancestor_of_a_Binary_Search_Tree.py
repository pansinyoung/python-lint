"""
1311. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}

图片

Example
Example 1:

Input:
{6,2,8,0,4,7,9,#,#,3,5}
2
8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input:
{6,2,8,0,4,7,9,#,#,3,5}
2
4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Notice
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
from typing import List
from collections import deque

"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        result = self.helper(root, p, q)
        return result[2] if result[0] and result[1] else None

    def helper(self, root, p, q):
        if not root:
            return False, False, root
        found_p, found_q, result = root == p, root == q, root
        (left_p, left_q, left) = self.helper(root.left, p, q)
        if left_p and left_q:
            return left_p, left_q, left
        (right_p, right_q, right) = self.helper(root.right, p, q)
        if right_p and right_q:
            return right_p, right_q, right
        return found_p or left_p or right_p, found_q or left_q or right_q, root

def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
