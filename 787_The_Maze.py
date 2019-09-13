"""
787. The Maze
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or
right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example
Example 1:

Input:
map =
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
Output:
false
Example 2:

Input:
map =
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [4,4]
Output:
true
Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
from typing import List


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        num_rows = len(maze)
        num_cols = len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * num_cols for _ in range(num_rows)]
        visited[start[0]][start[1]] = True
        que = [start]

        while que:
            cur = que.pop()
            for (x, y) in directions:
                temp = [cur[0], cur[1]]
                while 0 <= temp[0] < num_rows and 0 <= temp[1] < num_cols and maze[temp[0]][temp[1]] != 1:
                    temp[0] += x
                    temp[1] += y
                temp[0] -= x
                temp[1] -= y
                if temp[0] == destination[0] and temp[1] == destination[1]:
                    return True
                if not visited[temp[0]][temp[1]]:
                    que.append(temp)
                visited[temp[0]][temp[1]] = True
        return False


def main():
    s = Solution()
    map = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
    start = [0, 4]
    end = [3, 2]
    print(s.hasPath(map, start, end))


if __name__ == '__main__':
    main()


