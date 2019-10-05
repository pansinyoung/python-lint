"""
802. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the number 0.

You may assume that there will be only one unique solution.
"""


class Solution:
    def solveSudoku(self, board):
        print(self.helper(0, 0, board))

    def getPossibleNumber(self, x, y, board):
        if board[x][y] != 0:
            return []
        result = set([_ for _ in range(1, 10)])
        i = 0
        while i < 9:
            if i != x and board[i][y] in result:
                result.remove(board[i][y])
            if i != y and board[x][i] in result:
                result.remove(board[x][i])
            i += 1
        for i in range(0, 3) if x < 3 else range(3, 6) if x < 6 else range(6, 9):
            for j in range(0, 3) if y < 3 else range(3, 6) if y < 6 else range(6, 9):
                if i != x and j != y and board[i][j] in result:
                    result.remove(board[i][j])
        return result

    def helper(self, x, y, board):
        if x >= 9:
            return True
        if board[x][y] != 0:
            return self.helper(x + 1 if y == 8 else x, y + 1 if y < 8 else 0, board)
        next_nums = self.getPossibleNumber(x, y, board)
        while next_nums:
            board[x][y] = next_nums.pop()
            if self.helper(x + 1 if y == 8 else x, y + 1 if y < 8 else 0, board):
                return True
            board[x][y] = 0
        return False


if __name__ == '__main__':
    b = [[0, 0, 9, 7, 4, 8, 0, 0, 0],
         [7, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 1, 0, 9, 0, 0, 0],
         [0, 0, 7, 0, 0, 0, 2, 4, 0],
         [0, 6, 4, 0, 1, 0, 5, 9, 0],
         [0, 9, 8, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 8, 0, 3, 0, 2, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 0, 2, 7, 5, 9, 0, 0]]
    Solution().solveSudoku(b)
    for row in b:
        print(row)
