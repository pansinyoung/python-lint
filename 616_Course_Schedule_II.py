"""
616. Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
"""
from typing import List


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        directions = {i: [] for i in range(numCourses)}
        degree = {i: 0 for i in range(numCourses)}
        for [i, j] in prerequisites:
            if i not in directions[j]:
                directions[j].append(i)
                degree[i] += 1
        queue = []
        i = 0
        for k in degree:
            if degree[k] == 0:
                queue.append(k)
        while True:
            if i >= len(queue):
                break
            cur = queue[i]
            for j in directions[cur]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
            i += 1
        return queue if len(queue) == numCourses else []


def main():
    s = Solution()
    n = 2
    pre = [[1, 0]]
    print(s.findOrder(n, pre))


if __name__ == '__main__':
    main()
