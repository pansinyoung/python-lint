"""
376. Binary Tree Path Sum
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Example 1:

Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
Example 2:

Input:
{1,2,4,2,3}
3
Output: []
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
Notice we need to find all paths from root node to leaf nodes.
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
There is no one satisfying it.
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
    def binaryTreePathSum(self, root, target):
        result = []
        self.helper(root, [], 0, target, result)
        return result

    def helper(self, root, prev, prev_sum, target, result):
        if not root:
            return
        prev.append(root.val)

        if not root.left and not root.right and prev_sum + root.val == target:
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
