"""
596. Minimum Subtree
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.
"""

"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


import sys


class Solution:
    def findSum(self, root):
        cur_sum = root.val
        result_node = root
        left_sum, left_min_node, left_min_sum = self.findSum(root.left) if root.left else (0, None, 0)
        right_sum, right_min_node, right_min_sum = self.findSum(root.right) if root.right else (0, None, 0)
        cur_sum = left_sum + right_sum + cur_sum
        result_sum = cur_sum
        if left_min_node and left_min_sum < result_sum:
            result_node = left_min_node
            result_sum = left_min_sum
        if right_min_node and right_min_sum < result_sum:
            result_node = right_min_node
            result_sum = right_min_sum
        return cur_sum, result_node, result_sum

    def findSubtree(self, root):
        return self.findSum(root)[1]


def main():
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(s.findSubtree(root).val)


if __name__ == "__main__":
    main()
