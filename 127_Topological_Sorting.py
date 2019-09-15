"""
127. Topological Sorting
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

图片

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
"""
from collections import deque
from typing import List
"""
Definition for a Directed graph node
"""


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    # BFS
    # def topSort(self, graph: List[DirectedGraphNode]) -> List[int]:
    #     if not graph:
    #         return []
    #     degrees = {i: 0 for i in graph}
    #     for cur in graph:
    #         for i in cur.neighbors:
    #             degrees[i] += 1
    #     queue = deque()
    #     result = []
    #     for k in degrees:
    #         if degrees[k] == 0:
    #             queue.append(k)
    #     while queue:
    #         cur = queue.popleft()
    #         result.append(cur)
    #         for i in cur.neighbors:
    #             degrees[i] -= 1
    #             if degrees[i] == 0:
    #                 queue.append(i)
    #
    #     return result

    # DFS
    def topSort(self, graph: List[DirectedGraphNode]) -> List[int]:
        if not graph:
            return []
        degrees = {i: 0 for i in graph}
        for cur in graph:
            for i in cur.neighbors:
                degrees[i] += 1
        queue = []
        result = []
        for k in degrees:
            if degrees[k] == 0:
                queue.append(k)
        while queue:
            cur = queue.pop()
            result.append(cur)
            for i in cur.neighbors:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i)

        return result


def main():
    s = Solution()
    node0 = DirectedGraphNode(0)
    node1 = DirectedGraphNode(1)
    node2 = DirectedGraphNode(2)
    node3 = DirectedGraphNode(3)
    node4 = DirectedGraphNode(4)
    node0.neighbors.append(node2)
    node0.neighbors.append(node3)
    node1.neighbors.append(node0)
    node1.neighbors.append(node2)
    node1.neighbors.append(node3)
    node3.neighbors.append(node2)
    node4.neighbors.append(node1)
    node4.neighbors.append(node2)
    node4.neighbors.append(node3)

    for a in s.topSort([node0, node1, node2, node3, node4]):
        print(a.label)


if __name__ == '__main__':
    main()
