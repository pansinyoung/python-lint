"""
578. Lowest Common Ancestor III
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

Example
Example1

Input:
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7
5 8
Output:
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

Example2

Input:
{1}
1 1
Output:
1
Explanation:
The tree is just a node, whose value is 1.
Notice
node A or node B may not exist in tree.
Each node has a different value
"""
from typing import Tuple

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def lowestCommonAncestor3(self, root: TreeNode, A: TreeNode, B: TreeNode) -> TreeNode:
        has_a, has_b, node = self.helper(root, A, B)
        return self.helper(root, A, B)[2] if has_b and has_a else None

    def helper(self, root: TreeNode, A: TreeNode, B: TreeNode) -> Tuple:
        if not root:
            return False, False, None
        if root == A and root == B:
            return True, True, root

        left_A, left_B, left_node = (False, False, None) if not root.left else self.helper(root.left, A, B)

        if left_A and left_B:
            return True, True, left_node

        right_A, right_B, right_node = (False, False, None) if not root.right else self.helper(root.right, A, B)

        if right_A and right_B:
            return True, True, right_node

        result_A = left_A or right_A or root == A
        result_B = left_B or right_B or root == B

        return result_A, result_B, root




def main():
    s = Solution()
    list = ["zw", "zy"]
    print(s.alienOrder(list))


if __name__ == '__main__':
    main()
