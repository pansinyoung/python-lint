"""
178. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
Notice
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
from typing import List
from collections import deque

"""
Definition for a undirected graph node
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        if not nodes:
            return []
        result = []
        visited = {i: False for i in nodes}
        for n in nodes:
            if visited[n]:
                continue
            queue = deque()
            queue.append(n)
            temp = []
            while queue:
                cur = queue.popleft()
                if visited[cur]:
                    continue
                visited[cur] = True
                temp.append(cur.label)
                for i in cur.neighbors:
                    if not visited[i]:
                        queue.append(i)
            if len(temp) > 0:
                temp.sort()
                result.append(temp)
        return result



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
