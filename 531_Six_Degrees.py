"""
531. Six Degrees
Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction, from any other person in the world, so that a chain of "a friend of a friend"
statements can be made to connect any two people in a maximum of six steps.

Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.

Example
Example1

Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4
Output: 2
Explanation:
    1------2-----4
     \          /
      \        /
       \--3--/
Example2

Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
Output: -1
Explanation:
    1      2-----4
                 /
               /
              3
"""
from typing import List
from collections import deque

"""
Definition for Undirected graph node
"""


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph: List[UndirectedGraphNode], s: UndirectedGraphNode, t: UndirectedGraphNode) -> int:
        if not graph or s is None or t is None or not s.neighbors or not t.neighbors:
            return -1
        if s == t:
            return 0
        queue1 = deque()
        queue2 = deque()
        queue1.append(s)
        queue2.append(t)
        queue1.append('#')
        queue2.append('#')
        visited1 = {s: 0}
        visited2 = {t: 0}
        result = -1
        while queue1 and queue2:
            while queue1:
                cur = queue1.popleft()
                if cur == '#':
                    if queue1:
                        queue1.append('#')
                    break
                for n in cur.neighbors:
                    if n in visited2:
                        return visited1[cur] + 1 + visited2[n]
                    if n not in visited1:
                        visited1[n] = visited1[cur] + 1
                        queue1.append(n)
            while queue2:
                cur = queue2.popleft()
                if cur == '#':
                    if queue2:
                        queue2.append('#')
                    break
                for n in cur.neighbors:
                    if n in visited1:
                        return visited2[cur] + 1 + visited1[n]
                    if n not in visited2:
                        visited2[n] = visited2[cur] + 1
                        queue2.append(n)
        return result


def main():
    s = Solution()
    graph = []
    dict = {}
    string = "1,2#2,1,3#3,2,4#4,3,5#5,4,6#6,5,7#7,6,8#8,7,9#9,8,10#10,9,11#11,10,12#12,11,13#13,12"
    for i in string.split('#'):
        items = i.split(',')
        cur = UndirectedGraphNode(items[0])
        dict[cur.label] = cur
    for i in string.split('#'):
        items = i.split(',')
        for j in items[1:]:
            dict[items[0]].neighbors.append(dict[j])
    graph = list(dict.values())

    print(s.sixDegrees(graph, dict['12'], dict['1']))


if __name__ == '__main__':
    main()
