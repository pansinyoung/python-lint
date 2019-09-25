"""
900. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
Notice
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def closestValue(self, root, target):
        result = root.val
        if root.left:
            r_left = self.closestValue(root.left, target)
            result = result if abs(result - target) < abs(r_left - target) else r_left
        if root.right:
            r_right = self.closestValue(root.right, target)
            result = result if abs(result - target) < abs(r_right - target) else r_right
        return result


def main():
    s = Solution()

    print(s.dropEggs(1))


if __name__ == "__main__":
    main()
