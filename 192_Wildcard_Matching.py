"""
192. Wildcard Matching
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example
Example 1

Input:
"aa"
"a"
Output: false
Example 2

Input:
"aa"
"aa"
Output: true
Example 3

Input:
"aaa"
"aa"
Output: false
Example 4

Input:
"aa"
"*"
Output: true
Explanation: '*' can replace any string
Example 5

Input:
"aa"
"a*"
Output: true
Example 6

Input:
"ab"
"?*"
Output: true
Explanation: '?' -> 'a' '*' -> 'b'
Example 7

Input:
"aab"
"c*a*b"
Output: false
"""

class Solution:
    def isMatch(self, s, p):
        memo = {}
        result = self.helper(s, 0, p, 0, memo)
        return result

    def helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j >= len(p):
            result = i >= len(s)
        elif i >= len(s) and j < len(p):
            result = True
            while j < len(p):
                if p[j] != '*':
                    result = False
                    break
                j += 1
        else:
            if p[j] == '*':
                result = self.helper(s, i, p, j + 1, memo) or self.helper(s, i + 1, p, j, memo)
            else:
                result = (s[i] == p[j] or p[j] == '?') and self.helper(s, i + 1, p, j + 1, memo)
        memo[(i, j)] = result
        return result



if __name__ == '__main__':
    print(Solution().isMatch('bbabacccbcbbcaaab', '*a*b??b*b'))
