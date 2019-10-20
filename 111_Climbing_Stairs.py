"""
111. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example
Example 1:
	Input:  n = 3
	Output: 3

	Explanation:
	1) 1, 1, 1
	2) 1, 2
	3) 2, 1
	total 3.


Example 2:
	Input:  n = 1
	Output: 1

	Explanation:
	only 1 way.
"""


class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        temp1, temp2 = 1, 1
        for i in range(2, n + 1):
            temp1, temp2 = temp2, temp1 + temp2
        return temp2


print(Solution().climbStairs(4))
