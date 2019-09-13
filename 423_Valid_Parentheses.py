"""
423. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Example
Example 1:

Input: "([)]"
Output: False
Example 2:

Input: "()[]{}"
Output: True
Challenge
Use O(n) time, n is the number of parentheses.
"""


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        if not s:
            return True
        dictionary = {'}': '{', ')': '(', ']': '['}
        right_parentheses = ['}', ']', ')']
        stack = []
        for c in s:
            if c not in right_parentheses:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() is not dictionary[c]:
                    return False
        if len(stack) != 0:
            return False
        return True

def main():
    s = Solution()
    test1 = ''
    test2 = '()'
    test3 = '()[]{}'
    test4 = '({)}'
    test5 = '([)]'
    print(test1, s.isValidParentheses(test1))
    print(test2, s.isValidParentheses(test2))
    print(test3, s.isValidParentheses(test3))
    print(test4, s.isValidParentheses(test4))
    print(test5, s.isValidParentheses(test5))


if __name__ == '__main__':
    main()
