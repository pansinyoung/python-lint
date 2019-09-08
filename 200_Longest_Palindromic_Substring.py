"""
200. Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.

Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"
Example 2:

Input:"aba"
Output:"aba"
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
"""


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        result = ''
        for i in range(len(s)):
            r1 = self.find_longest_palindrome(s, i, i)
            r2 = self.find_longest_palindrome(s, i, i + 1) if i + 1 < len(s) else ''
            result = r1 if len(r1) > len(result) else result
            result = r2 if len(r2) > len(result) else result

        return result

    def find_longest_palindrome(self, s: str, start: int, end: int) -> str:
        if s[start] != s[end]:
            return ''
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]


def main():
    a = 'abcdzdcab'
    b = ''
    c = 'aba'
    d = '1a2'
    s = Solution()
    print(s.longestPalindrome(a))
    print(s.longestPalindrome(b))
    print(s.longestPalindrome(c))
    print(s.longestPalindrome(d))


if __name__ == '__main__':
    main()