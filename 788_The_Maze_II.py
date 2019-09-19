"""
788. The Maze II
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops,
it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by
the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are
represented by row and column indexes.

Example
Example 1:
	Input:
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (4,4)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  12

	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

Example 2:
	Input:
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (0,0)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  6

	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)

Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
from typing import List
from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def get_move(self, start: tuple, maze: List[List[int]]):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        for dir in directions:
            i, j = start[0] + dir[0], start[1] + dir[1]
            while 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0:
                i, j = i + dir[0], j + dir[1]
            i, j = i - dir[0], j - dir[1]
            if i != start[0] or j != start[1]:
                result.append((i, j))
        return result

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]):
        result = -1
        queue1 = deque()
        visited1 = [[-1] * len(maze[0]) for _ in range(len(maze))]
        queue1.append((start[0], start[1]))
        visited1[start[0]][start[1]] = 0
        while queue1:
            cur = queue1.popleft()
            for (i, j) in self.get_move(cur, maze):
                step = visited1[cur[0]][cur[1]] + abs((i - cur[0]) + (j - cur[1]))
                if destination == [i, j]:
                    result = min(step, result) if result >= 0 else step
                elif visited1[i][j] >= 0:
                    visited1[i][j] = min(step, visited1[i][j])
                else:
                    visited1[i][j] = step
                    queue1.append((i, j))
        return result


def main():
    s = Solution()
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start = [0, 4]
    destination = [4, 4]
    print(s.shortestDistance(maze, start, destination))


if __name__ == '__main__':
    main()
