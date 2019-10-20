"""
515. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Example
Example 1:

Input: [[14,2,11],[11,14,5],[14,3,10]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: [[1,2,3],[1,4,6]]
Output: 3
Notice
All costs are positive integers.
"""

class Solution:
    def minCost(self, costs):
        if not costs:
            return 0
        dp = [[-1] * 3 for _ in costs]
        return min(dp[0])

    def helper(self, costs, index, dp, prev):
        if index >= len(costs):
            return
        if index == len(costs) - 1:
            for i in range(3):
                dp[index][i] = costs[index][i]
            return
        r = [0, 1, 2] if index == 0 else [i for i in range(3) if prev[index - 1] != i]
        for i in r:
            for j in range(3):
                if dp[index + 1][j] > 0:
                    continue
                prev.append(i)
                self.helper(costs, index + 1, dp, prev)
                prev.pop()
            dp[index][i] = min([dp[index + 1][j] + costs[index][i] for j in range(3) if j != i])
