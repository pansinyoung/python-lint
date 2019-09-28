"""
901. Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Example
Example 1:

Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1
Example 2:

Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2
Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Notice
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
​​
"""
from typing import List

"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        lower = self.get_stack(root, target)
        upper = list(lower)

        if lower[-1].val < target:
            self.move_upper(upper)
        else:
            self.move_lower(lower)

        result = []
        for i in range(k):
            if self.is_lower_close(lower, upper, target):
                result.append(lower[-1].val)
                self.move_lower(lower)
            else:
                result.append(upper[-1].val)
                self.move_upper(upper)
        return result

    def get_stack(self, root: TreeNode, target: float) -> List[TreeNode]:
        stack = []
        node = root
        while node:
            stack.append(node)
            if node.val > target:
                node = node.left
            else:
                node = node.right
        return stack

    def move_lower(self, stack: List[TreeNode]):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()

    def move_upper(self, stack: List[TreeNode]):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()

    def is_lower_close(self, lower_stack: List[TreeNode], upper_stack: List[TreeNode], target: float) -> bool:
        if not lower_stack:
            return False
        if not upper_stack:
            return True
        return target - lower_stack[-1].val < upper_stack[-1].val - target


def main():
    s = Solution()
    A = [1, 2, 3, 4, 5, 6, 7, 8, 10, 100, 150, 156, 179]
    target = 9
    k = 12
    print(s.kClosestNumbers(A, target, k))


if __name__ == '__main__':
    main()
