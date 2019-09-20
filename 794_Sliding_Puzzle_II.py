"""
794. Sliding Puzzle II
中文English
On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.

If it is impossible to move from initial state to final state, return -1.

Example
Example 1:

Input:
[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Output:
4

Explanation:
[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]
Example 2：

Input:
[[2,3,8],[7,0,5],[1,6,4]]
[[1,2,3],[8,0,4],[7,6,5]]
Output:
-1
Challenge
How to optimize the memory?
Can you solve it with A* algorithm?
"""
from typing import List
from collections import deque


class Solution:
    def matrix_to_string(self, matrix: List[List[int]]):
        if not matrix:
            return ''
        return ''.join(str(x) for i in matrix for x in i)

    def get_next_moves(self, s: str) -> List[str]:
        for i in range(9):
            if s[i] == '0':
                break
        result = []
        if i - 3 >= 0:
            result.append(s[:i - 3] + s[i] + s[i - 2:i] + s[i - 3] + s[i + 1:])
        if i - 1 >= 0 and i // 3 == (i - 1) // 3:
            result.append(s[:i - 1] + s[i] + s[i - 1] + s[i + 1:])
        if i + 3 < 9:
            result.append(s[:i] + s[i + 3] + s[i + 1: i + 3] + s[i] + s[i + 4:])
        if i + 1 < 9 and (i + 1) // 3 == i // 3:
            result.append(s[:i] + s[i + 1] + s[i] + s[i + 2:])
        return result

    def minMoveStep(self, init_state: List[List[int]], final_state: List[List[int]]) -> int:
        init_string = self.matrix_to_string(init_state)
        final_string = self.matrix_to_string(final_state)
        if init_string == final_string:
            return 0
        queue = deque()
        queue.append(init_string)
        visited = set()
        step = 0
        while queue:
            print(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == final_string:
                    print(cur)
                    return step
                for i in self.get_next_moves(cur):
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
            step += 1
        return -1


def main():
    s = Solution()
    source = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    print(s.minMoveStep(source, target))


if __name__ == '__main__':
    main()
