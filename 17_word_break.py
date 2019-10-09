"""
107. Word Break
Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.

Example
Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true
"""


class Solution:
    def wordBreak(self, s, dict):
        n = len(s)
        lengths = set([len(d) for d in dict])
        mem = [False] * (n + 1)
        mem[0] = True
        for i in range(1, n + 1):
            if not mem[i - 1]:
                continue
            for l in lengths:
                if i + l - 1 <= n and s[i - 1: i + l - 1] in dict:
                    mem[i + l - 1] = True
            print(mem)
        return mem[n]


if __name__ == '__main__':
    print(Solution().wordBreak('cars', ["car","ca","rs"]))
