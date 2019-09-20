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


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0 or (n == 1 and len(edges) == 0):
            return True
        if n != len(edges) + 1:
            return False
        degrees = [0 for _ in range(n)]
        edge = [[] for _ in range(n)]
        for [i, j] in edges:
            edge[i].append(j)
            edge[j].append(i)
            degrees[i] += 1
            degrees[j] += 1
        queue = deque()
        for i in range(n):
            if degrees[i] == 0:
                return False
            if degrees[i] == 1:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            for i in edge[cur]:
                degrees[i] -= 1
                if degrees[i] == 1:
                    queue.append(i)
        return degrees == [0] * n


def main():
    s = Solution()
    n = 1
    edges = []
    print(s.validTree(n, edges))


if __name__ == '__main__':
    main()
