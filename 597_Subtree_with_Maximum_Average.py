"""
597. Subtree with Maximum Average
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
The average of subtree of 11 is 4.3333, is the maximun.
Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.
"""
from typing import List
from collections import deque

"""
Definition of TreeNode:
"""
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def findSubtree2(self, root):
        if not root:
            return None
        else:
            return self.helper(root)[3]

    # return (cur_count, cur_sum, max_avg, node)
    def helper(self, root):
        if not root.left and not root.right:
            return 1, root.val, root.val, root
        cur_avg, cur_sum, cur_count = root.val, root.val, 1
        (left_count, left_sum, left_max, left_node) = self.helper(root.left) if root.left else (0, 0, -sys.maxsize, None)
        (right_count, right_sum, right_max, right_node) = self.helper(root.right) if root.right else (0, 0, -sys.maxsize, None)
        cur_count += left_count + right_count
        cur_sum += left_sum + right_sum
        cur_avg = cur_sum / cur_count
        result_node = root if cur_avg > left_max and cur_avg > right_max else left_node if left_max > right_max else right_node
        return cur_count, cur_sum, max(left_max, right_max, cur_avg), result_node



def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
