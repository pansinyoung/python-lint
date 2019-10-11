"""
476. Stone Game
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Example
Example 1:

Input: [3, 4, 3]
Output: 17
Example 2:

Input: [4, 1, 1, 4]
Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
"""


class Solution:
    def stoneGame(self, A):
        n = len(A)
        interval = 0
        memo = [[0] * n for _ in range(n)]
        sum = [[0] * n for _ in range(n)]
        while interval < n:
            i, j = 0, interval
            while j < n:
                if interval == 0:
                    sum[i][j] = A[i]
                elif interval == 1:
                    sum[i][j] = sum[i][j - 1] + A[j]
                    memo[i][j] = sum[i][j]
                else:
                    sum[i][j] = sum[i][j - 1] + A[j]
                    memo[i][j] = min([(memo[i][k - 1] + memo[k][j] + sum[i][k - 1] + sum[k][j]) for k in range(i + 1, j + 1)])
                i += 1
                j += 1
            interval += 1
        return memo[0][n - 1]


if __name__ == '__main__':
    print(Solution().stoneGame([4, 1, 1, 4]))
