"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example
Example 1:

Input:
{1,2,3}
Output:
[[2,3],[1]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}
level order traversal
Example 2:

Input:
{3,9,20,#,#,15,7}
Output:
[[15,7],[9,20],[3]]
Explanation:
    3
   / \
  9  20
    /  \
   15   7
it will be serialized {3,9,20,#,#,15,7}
level order traversal
"""
from typing import List
from collections import deque

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tree_queue = deque()
        tree_queue.append(root)
        tree_queue.append('#')
        res = deque()
        cur_list = []
        while tree_queue:
            cur = tree_queue.popleft()
            if cur == '#':
                res.appendleft(cur_list)
                cur_list = []
                if tree_queue:
                    tree_queue.append('#')
            else:
                cur_list.append(cur.val)
                if cur.left:
                    tree_queue.append(cur.left)
                if cur.right:
                    tree_queue.append(cur.right)
        return list(res)


def main():
    s = Solution()
    graph = []
    dict = {}
    string = "-20,-2,6#-19,13#-18#-17,1,2,-10,-11#-16,1#-15,-13,11,1,-7#-14,-13,-9,3,18#-13,-15,-14#-12,-2#-11,-17,5#-10,-17#-9,5,-14,-1,0#-8,2#-7,16,-5,-15#-6#-5,14,7,-7#-4,-2#-3,14#-2,-12,-20,8,-4,12#-1,-9#0,-9#1,-16,-17,-15#2,12,-8,-17#3,-14,13#4,4,4#5,-9,17,-11#6,-20,15,8#7,-5#8,-2,6,11#9,17#10,16#11,18,-15,8#12,2,-2#13,-19,3#14,-5,-3#15,6#16,-7,10#17,9,5#18,11,-14#19"
    for i in string.split('#'):
        items = i.split(',')
        cur = UndirectedGraphNode(int(items[0]))
        dict[cur.label] = cur
    for i in string.split('#'):
        items = i.split(',')
        for j in items[1:]:
            # print(items)
            dict[int(items[0])].neighbors.append(dict[int(j)])
    graph = list(dict.values())

    print(s.connectedSet(graph))


if __name__ == '__main__':
    main()
