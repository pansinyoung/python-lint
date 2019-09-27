"""
480. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

Example
Example 1:

Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5
Example 2:

Input：{1,2}
Output：["1->2"]
Explanation：
   1
 /
2
"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return ['']
        return self.getPath(root, '')

    def getPath(self, root: TreeNode, prev: str) -> List[str]:
        cur = prev + '->' + str(root.val) if not prev else str(root.val)
        if not root.left and not root.right:
            return [cur]
        result = []
        if root.left:
            result += self.getPath(root.left, cur)
        if root.right:
            result += self.getPath(root.right, cur)
        return result


def main():
    s = Solution()
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # print(s.serialize(None))
    # print(s.serialize(s.deserialize(s.serialize(None))))


if __name__ == '__main__':
    main()
