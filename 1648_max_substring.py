"""
1648. max substring
Given a string s, return the last substring of s in lexicographical order.

Example
Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
The lexicographically maximum substring is "bab".
Example 2:

Input: "baca"
Output: "ca"
Notice
1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""


class Solution:
    def maxSubstring(self, s):
        if not s:
            return s
        n = len(s)
        prefix = s[0]
        max_indexes = [_ for _ in range(n)]
        interval = 0
        new = []
        while len(max_indexes) > 1:
            while max_indexes:
                cur = max_indexes.pop()
                if cur + interval < n and s[cur: cur + interval + 1] >= prefix:
                    prefix = s[cur: cur + interval + 1]
                    new.append(cur)
            interval += 1
            max_indexes = new[:]
            new = []

        return max_indexes


if __name__ == '__main__':
    print(Solution().maxSubstring('cccbacasdfbadfsgcccb'))
