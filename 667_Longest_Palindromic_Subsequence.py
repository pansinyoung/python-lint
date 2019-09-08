"""
667. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is
1000.

Example
Example1

Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
Example2

Input: "bbbbb"
Output: 5
"""

from typing import Dict

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return len(s)
        return self.find_longest_palindrome_subsequence(s, 0, len(s) - 1, {})

    def find_longest_palindrome_subsequence(self, s: str, start: int, end: int, mem: Dict) -> int:
        if (start, end) in mem:
            return mem[(start, end)]
        if start > end:
            return 0
        if start == end:
            mem[(start, end)] = 1
            return 1
        if s[start] == s[end]:
            mem[(start, end)] = 2 + self.find_longest_palindrome_subsequence(s, start + 1, end - 1, mem)
            return mem[(start, end)]
        else:
            mem[(start, end)] = max(self.find_longest_palindrome_subsequence(s, start + 1, end, mem),
                                    self.find_longest_palindrome_subsequence(s, start, end - 1, mem))
            return mem[(start, end)]


def main():
    a = 'asdasdajjdkajwiejladjkahsdjhawiueauwhdjashdjancnkjsahduiawudhajsnhsjahjdhawuahdjshjnzanjcnhjdashuawhdjaksndjkahduwhwauhdai'
    b = ''
    c = 'bbbbb'
    d = '1a2'
    s = Solution()
    print(s.longestPalindromeSubseq(a))
    print(s.longestPalindromeSubseq(b))
    print(s.longestPalindromeSubseq(c))
    print(s.longestPalindromeSubseq(d))


if __name__ == '__main__':
    main()