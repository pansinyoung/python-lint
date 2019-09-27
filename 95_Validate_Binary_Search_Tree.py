"""
95. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
Example 1:

Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
Example 2:

Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
"""
from typing import Tuple

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        return self.helper(root)[2]

    def helper(self, root: TreeNode) -> Tuple:
        left_min, left_max, left_is_bst = self.helper(root.left) if root.left else (root.val, root.val, True)
        if not left_is_bst:
            return root.val, root.val, False
        right_min, right_max, right_is_bst = self.helper(root.right) if root.right else (root.val, root.val, True)
        if not right_is_bst:
            return root.val, root.val, False
        return left_min, right_max, left_max < root.val < right_min

def main():
    s = Solution()
    list = ["zw", "zy"]
    print(s.alienOrder(list))


if __name__ == '__main__':
    main()
