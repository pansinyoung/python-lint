"""
622. Frog Jump
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Example
Example 1:

Given stones = [0,1,3,5,6,8,12,17]
Input:
[0,1,3,5,6,8,12,17]
Output:
true

Explanation:
There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,third stone at the 3rd unit, and so on...The last stone at the 17th unit.
Return true. The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Given stones = `[0,1,2,3,4,8,9,11]`
Input:
[0,1,2,3,4,8,9,11]
Output:
false

Explanation:
Return false. There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
Notice
The number of stones is ≥ 2 and is < 1100.
Each stone's position will be a non-negative integer < 2^31.
The first stone's position is always 0.
"""


class Solution:
    def canCross(self, stones):
        dp = {}
        for s in stones:
            dp[s] = set()
        dp[0].add(0)
        for s in stones:
            for k in dp[s]:
                if k - 1 > 0 and s + k - 1 in dp:
                    dp[s + k - 1].add(k - 1)

                if k > 0 and s + k in dp:
                    dp[s + k].add(k)

                if s + k + 1 in dp:
                    dp[s + k + 1].add(k + 1)
        return len(dp[stones[-1]]) > 0
