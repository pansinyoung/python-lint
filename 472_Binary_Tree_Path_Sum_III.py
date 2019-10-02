"""
246. Binary Tree Path Sum II
Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must go in a straight line down.

Example
Example 1:

Input:
{1,2,3,4,#,2}
6
Output:
[[2, 4],[1, 3, 2]]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   /
4   2
for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
Example 2:

Input:
{1,2,3,4}
10
Output:
[]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
"""
from typing import List
from collections import deque

"""
Definition of TreeNode:
"""


class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    def binaryTreePathSum3(self, root, target):
        result = []
        self.node_finder(root, target, result)

        return result

    def node_finder(self, root, target, result):
        if not root:
            return

        self.path_finder(root, None, [], target, result)
        self.node_finder(root.left, target, result)
        self.node_finder(root.right, target, result)

    def path_finder(self, root, prev_node, path, target, result):
        path.append(root.val)
        target -= root.val

        if target == 0:
            result.append(path[:])

        if root.parent not in [None, prev_node]:
            self.path_finder(root.parent, root, path, target, result)

        if root.left not in [None, prev_node]:
            self.path_finder(root.left, root, path, target, result)

        if root.right not in [None, prev_node]:
            self.path_finder(root.right, root, path, target, result)

        path.pop()


def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
