"""
427. Generate Parentheses
Given n, and there are n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example
Example 1:

Input: 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Example 2:

Input: 2
Output: ["()()", "(())"]
"""


class Solution:
    def generateParenthesis(self, n):
        result = []
        self.helper(n, 0, 0, "", result)
        return result

    def helper(self, n, left, right, prev, result):
        if left == right == n:
            result.append(prev)
            return
        if left == n:
            result.append(prev + ')' * (left - right))
            return
        self.helper(n, left + 1, right, prev + '(', result)
        if right < left:
            self.helper(n, left, right + 1, prev + ')', result)


if __name__ == '__main__':
    print(Solution().generateParenthesis(2))
