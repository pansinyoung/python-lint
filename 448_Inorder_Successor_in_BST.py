"""
448. Inorder Successor in BST
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.

Example
Example 1:

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
Example 2:

Input: {2,1,3}, node with value 1
Output: 2
Explanation:
    2
   / \
  1   3
Binary Tree Representation

Challenge
O(h), where h is the height of the BST.

Notice
It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)
"""


class Solution:
    def inorderSuccessor(self, root, p):
        path = self.get_path(root, [], p)
        self.move_upper(path)
        return path[-1] if path else None

    def get_path(self, root, prev, p):
        if not root or not p:
            return []
        if root == p:
            return prev + [p]
        return self.get_path(root.left if p.val < root.val else root.right, prev + [root], p)

    def move_lower(self, path):
        if not path:
            return []
        cur = path.pop()
        if cur.left:
            cur = cur.left
            while cur:
                path.append(cur)
                cur = cur.right
        else:
            while path and path[-1].left == cur:
                cur = path.pop()

    def move_upper(self, path):
        if not path:
            return []
        cur = path.pop()
        if cur.right:
            cur = cur.right
            while cur:
                path.append(cur)
                cur = cur.left
        else:
            while path and path[-1].right == cur:
                cur = path.pop()


def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
