"""
68. Binary Tree Postorder Traversal
中文English
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Example 1:

Input：{1,2,3}
Output：[2,3,1]
Explanation:
   1
  / \
 2   3
 it will be serialized {1,2,3}
Post order traversal
Example 2:

Input：{1,#,2,3}
Output：[3,2,1]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Post order traversal
Challenge
Can you do it without recursion?

Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import collections

class Solution:
    def postorderTraversal(self, root):
        # non - recursive
        # return self.traverse(root)

        return self.recursive(root)

    def recursive(self, root):
        if not root:
            return []
        return self.recursive(root.left) + self.recursive(root.right) + [root.val]

    def traverse(self, root):
        stack = [root]
        result = collections.deque()
        while stack:
            cur = stack.pop()
            result.appendleft(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return list(result)
            


def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
