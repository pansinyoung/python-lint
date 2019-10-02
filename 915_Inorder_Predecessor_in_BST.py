"""
915. Inorder Predecessor in BST
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

Example
Example1

Input: root = {2,1,3}, p = 1
Output: null
Example2

Input: root = {2,1}, p = 2
Output: 1
Notice
If the given node has no in-order predecessor in the tree, return null
"""


class Solution:
    def inorderPredecessor(self, root, p):
        path = self.get_path(root, [], p)
        self.move_lower(path)
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


def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
