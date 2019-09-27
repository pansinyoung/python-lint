"""
93. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Example  1:
	Input: tree = {1,2,3}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  1
		 / \
		2  3


Example  2:
	Input: tree = {3,9,20,#,#,15,7}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  3
		 / \
		9  20
		  /  \
		 15   7


Example  3:
	Input: tree = {1,#,2,3,4}
	Output: false

	Explanation:
	This is not a balanced tree.
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1
		   \
		   2
		  /  \
		 3   4
"""
from typing import Tuple


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left_bal, left_dep = self.get_depth(root.left)
        right_bal, right_dep = self.get_depth(root.right)
        if not left_bal or not right_bal or abs(left_dep - right_dep) > 1:
            return False
        return True

    def get_depth(self, root: TreeNode) -> Tuple:
        if not root:
            return True, 0
        left_bal, left_depth = True, 0
        if root.left:
            left_bal, left_depth = self.get_depth(root.left)
            if not left_bal:
                return False, 0
        right_bal, right_dep = True, 0
        if root.right:
            right_bal, right_dep = self.get_depth(root.right)
            if not right_bal:
                return False, 0
        if abs(left_depth - right_dep) > 1:
            return False, 0
        return True, max(right_dep, left_depth) + 1


def main():
    s = Solution()
    test = ArrayReader([1, 3, 3, 3, 6, 9, 21])
    target = 122
    print(s.searchBigSortedArray(test, target))


if __name__ == '__main__':
    main()
