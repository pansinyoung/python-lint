"""
611. Knight Shortest Path
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output:-1
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Notice
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
"""
"""
Definition for a point.
"""
from collections import deque

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        if grid[source.x][source.y] == 1 or grid[destination.x][destination.y] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        queue, queue2, path_dict, path_dict2 = deque(), deque(), set(), set()
        step = -1
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        queue.append((source.x, source.y))
        queue2.append((destination.x, destination.y))
        while queue and queue2:
            step += 1
            for _ in range(len(queue)):
                curx, cury = queue.popleft()
                if (curx, cury) in path_dict2:
                    return step
                for dx, dy in directions:
                    new_x = curx + dx
                    new_y = cury + dy
                    if (new_x, new_y) in path_dict:
                        continue
                    if new_x in range(0, m) and new_y in range(0, n) and grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y))
                        path_dict.add((new_x, new_y))

            step += 1
            for _ in range(len(queue2)):
                curx, cury = queue2.popleft()
                if (curx, cury) in path_dict:
                    return step
                for dx, dy in directions:
                    new_x = curx + dx
                    new_y = cury + dy
                    if (new_x, new_y) in path_dict2:
                        continue
                    if new_x in range(0, m) and new_y in range(0, n) and grid[new_x][new_y] == 0:
                            queue2.append((new_x, new_y))
                            path_dict2.add((new_x, new_y))
        return -1


def main():
    s = Solution()
    test1 = [[0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1], [0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1],
             [0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1]]
    # test1 = [[0, 0, 0],
    #          [0, 0, 0],
    #          [0, 0, 0]]
    source = Point(0, 0)
    destination = Point(7, 0)
    print(s.shortestPath(test1, source, destination))


if __name__ == '__main__':
    main()
