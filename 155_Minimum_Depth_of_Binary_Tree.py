"""
155. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example
Example 1:

Input: {}
Output: 0
Example 2:

Input:  {1,#,2,3}
Output: 3
Explanation:
	1
	 \
	  2
	 /
	3
it will be serialized {1,#,2,3}
Example 3:

Input:  {1,2,3,#,#,4,5}
Output: 2
Explanation:
      1
     / \
    2   3
       / \
      4   5
it will be serialized {1,2,3,#,#,4,5}
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
    def minDepth(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left, right = self.dfs(root.left), self.dfs(root.right)
        return min(left, right) + 1

def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
