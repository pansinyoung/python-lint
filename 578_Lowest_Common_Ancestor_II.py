"""
474. Lowest Common Ancestor II
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

The node has an extra attribute parent which point to the father of itself. The root's parent is null.

Example
Example 1:

Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
     4
     / \
    3   7
       / \
      5   6
LCA(3, 5) = 4
Example 2:

Input：{4,3,7,#,#,5,6},5,6
Output：7
Explanation：
      4
     / \
    3   7
       / \
      5   6
LCA(5, 6) = 7
"""
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:

    def lowestCommonAncestorII(self, root: TreeNode, A: TreeNode, B: TreeNode) -> TreeNode:
        path_A = self.helper(root, A, [])
        path_B = self.helper(root, B, [])
        result = None
        i_A = len(path_A) - 1
        i_B = len(path_B) - 1

        while i_A >= 0 and i_B >= 0:
            if path_A[i_A] != path_B[i_B]:
                break
            result = path_A[i_A]
            i_A -= 1
            i_B -= 1

        return result

    def helper(self, root: TreeNode, target: TreeNode, path: List) -> List:
        cur = path + [target]
        if target == root:
            return cur
        return self.helper(root, target.parent, cur)


def main():
    s = Solution()
    list = ["zw", "zy"]
    print(s.alienOrder(list))


if __name__ == '__main__':
    main()
