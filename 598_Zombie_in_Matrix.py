"""
598. Zombie in Matrix
中文English
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the
nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all
people into zombies? Return -1 if can not turn all people into zombies.

Example
Example 1:

Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
Example 2:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
"""
from typing import List
from collections import deque


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def has_human(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return True
        return False

    def zombie(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        queue = deque()
        result = 0
        has_human = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                if grid[i][j] == 0:
                    has_human = True

        queue.append('#')

        while has_human:
            if not queue:
                return -1
            result += 1
            while queue:
                cur = queue.popleft()
                if cur == '#':
                    if queue:
                        queue.append('#')
                    break
                for d in directions:
                    if cur[0] + d[0] in range(m) \
                            and cur[1] + d[1] in range(n) \
                            and grid[cur[0] + d[0]][cur[1] + d[1]] == 0:
                        grid[cur[0] + d[0]][cur[1] + d[1]] = 1
                        queue.append((cur[0] + d[0], cur[1] + d[1]))
            has_human = self.has_human(grid)
        return result


def main():
    s = Solution()
    source = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 1]]
    print(s.zombie(source))


if __name__ == '__main__':
    main()
