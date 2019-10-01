"""
66. Binary Tree Preorder Traversal
中文English
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Example 1:

Input：{1,2,3}
Output：[1,2,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Preorder traversal
Example 2:

Input：{1,#,2,3}
Output：[1,2,3]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Preorder traversal
Challenge
Can you do it without recursion?

Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import collections

class Solution:
    def preorderTraversal(self, root):
        # non - recursive
        # return self.traverse(root)

        return self.recursive(root)

    def recursive(self, root):
        if not root:
            return []
        return [root.val] + self.recursive(root.left) + self.recursive(root.right)

    def traverse(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result
            


def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
