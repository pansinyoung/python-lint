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


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def binaryTreePathSum2(self, root, target):
        result = []
        self.helper(root, [], 0, target, result)
        return result

    def helper(self, root, prev, prev_sum, target, result):
        if not root:
            return

        if prev:
            self.helper(root.left, [], 0, target, result)
            self.helper(root.right, [], 0, target, result)

        prev.append(root.val)

        if prev_sum + root.val == target:
            result.append(list(prev))
        self.helper(root.left, prev, prev_sum + root.val, target, result)
        self.helper(root.right, prev, prev_sum + root.val, target, result)

        prev.pop()


def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
