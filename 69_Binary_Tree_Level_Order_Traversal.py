"""
69. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Example 1:

Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal
Example 2:

Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.

Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root, '/']
        i = 0
        while i < len(queue):
            if queue[i] == '/':
                if i == len(queue) - 1:
                    break
                else:
                    queue.append('/')
            else:
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            i += 1
        cur = []
        result = []
        for n in queue:
            if n == '/':
                result.append(cur)
                cur = []
            else:
                cur.append(n.val)

        return result

def main():
    s = Solution()

    # print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
