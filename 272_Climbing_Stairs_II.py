"""
272. Climbing Stairs II
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

Example
Example 1:

Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Example 2:

Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
Clarification
For n=0, we think the answer is 1.
"""


class Solution:
    def climbStairs2(self, n):
        temp1, temp2, temp3 = 1, 1, 2
        if n <= 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n + 1):
            temp1, temp2, temp3 = temp2, temp3, sum([temp1, temp2, temp3])
        return temp3


print(Solution().climbStairs2(5))
