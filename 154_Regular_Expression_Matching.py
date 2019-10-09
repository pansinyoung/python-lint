"""
154. Regular Expression Matching
中文English
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


The function prototype should be:

bool isMatch(string s, string p)

isMatch("aa","a") → false

isMatch("aa","aa") → true

isMatch("aaa","aa") → false

isMatch("aa", "a*") → true

isMatch("aa", ".*") → true

isMatch("ab", ".*") → true

isMatch("aab", "c*a*b") → true

Example
Example 1:

Input："aa"，"a"
Output：false
Explanation：
unable to match
Example 2:

Input："aa"，"a*"
Output：true
Explanation：
'*' can repeat a
"""


class Solution:
    def isMatch(self, s, p):
        return self.helper(s, 0, p, 0, {})

    def helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j >= len(p):
            result = i >= len(s)
        elif i >= len(s) and j < len(p):
            result = True
            while j < len(p):
                if p[j] != '*' and (j == len(p) - 1 or p[j + 1] != '*'):
                    result = False
                    break
                j += 1
        else:
            if j + 1 < len(p) and p[j + 1] == '*':
                result = self.helper(s, i, p, j + 1, memo)
            elif p[j] == '*':
                result = self.helper(s, i, p, j + 1, memo) or ((s[i] == p[j - 1] or p[j - 1] == '.') and self.helper(s, i + 1, p, j, memo))
            else:
                result = (s[i] == p[j] or p[j] == '.') and self.helper(s, i + 1, p, j + 1, memo)
        memo[(i, j)] = result
        return result


if __name__ == '__main__':
    print(Solution().isMatch('ad', 'aab*c*d*'))
