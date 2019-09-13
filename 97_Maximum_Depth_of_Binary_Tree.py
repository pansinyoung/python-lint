"""
97. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Example 1:

Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
Example 2:

Input: tree = {1,2,3,#,#,4,5}
Output: 3
Explanation: Like this:
   1
  / \
 2   3
    / \
   4   5
it will be serialized {1,2,3,#,#,4,5}
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def main():
    s = Solution()
    # print(test5, s.isValidParentheses(test5))


if __name__ == '__main__':
    main()
