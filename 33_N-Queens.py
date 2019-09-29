"""
33. N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other(Any two queens can't be in the same row, column, diagonal line).

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example
Example 1:

Input:1
Output:
   [["Q"]]


Example 2:

Input:4
Output:
[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
"""
from collections import deque


class Solution:
    def solveNQueens(self, n):
        if not n:
            return []
        if n == 1:
            return [['Q']]
        return self.nonRecursive(n)

    def nonRecursive(self, n):
        queue = deque()
        result = []
        queue.append(([["."] * n for _ in range(n)], 0, [], [], []))
        while queue:
            cur = queue.pop()
            if cur[1] == n:
                result.append([''.join(r) for r in cur[0]])
                continue
            for i in range(n):
                if cur[0][cur[1]][i] == '.' and i not in cur[2] and cur[1] - i not in cur[3] and cur[1] + i not in cur[4]:
                    new_list = [row[:] for row in cur[0]]
                    new_list[cur[1]][i] = 'Q'
                    queue.append((new_list, cur[1] + 1, cur[2] + [i], cur[3] + [cur[1] - i], cur[4] + [cur[1] + i]))
        return result


        # #recursive
        # result = []
        # self.recursive(n, [["."] * n for _ in range(n)], 0, result, set(), set(), set())
        # return result

    # def recursive(self, n, prev, row, result, visited_col, visited_diagon1, visited_diagon2):
    #     print(prev, row, result)
    #     if row >= n:
    #         result.append([''.join(r) for r in prev])
    #         return
    #     for i in range(n):
    #         if i not in visited_col and row - i not in visited_diagon1 and i + row not in visited_diagon2:
    #             prev[row][i] = 'Q'
    #             visited_col.add(i)
    #             visited_diagon1.add(row - i)
    #             visited_diagon2.add(i + row)
    #             self.recursive(n, prev, row + 1, result, visited_col, visited_diagon1, visited_diagon2)
    #             prev[row][i] = '.'
    #             visited_col.remove(i)
    #             visited_diagon1.remove(row - i)
    #             visited_diagon2.remove(i + row)


def main():
    s = Solution()
    print(s.solveNQueens(10))


if __name__ == '__main__':
    main()
