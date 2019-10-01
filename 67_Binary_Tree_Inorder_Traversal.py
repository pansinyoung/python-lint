"""
67. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Example 1:

Input：{1,2,3}
Output：[2,1,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Inorder Traversal
Example 2:

Input：{1,#,2,3}
Output：[1,3,2]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Inorder Traversal
Challenge
Can you do it without recursion?
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import collections

class Solution:
    def inorderTraversal(self, root):
        # non - recursive
        # return self.traverse(root)

        return self.recursive(root)

    def recursive(self, root):
        if not root:
            return []
        return self.recursive(root.left) + [root.val] + self.recursive(root.right)

    def traverse(self, root):
        if not root:
            return []
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return result
            


def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
