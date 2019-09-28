"""
86. Binary Search Tree Iterator
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Example
Example 1

Input:  {10,1,11,#,6,#,12}
Output:  [1, 6, 10, 11, 12]
Explanation:
The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
Example 2

Input: {2,1,3}
Output: [1,2,3]
Explanation:
The BST is look like this:
  2
 / \
1   3
You can return the inorder traversal of a BST tree [1,2,3]
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
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


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """
    def next(self):
        temp = self.stack.pop()
        self.helper(temp)
        return temp

    def helper(self, node):
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left




def main():
    s = Solution()
    A = [1, 2, 3, 4, 5, 6, 7, 8, 10, 100, 150, 156, 179]
    target = 9
    k = 12
    print(s.kClosestNumbers(A, target, k))


if __name__ == '__main__':
    main()
