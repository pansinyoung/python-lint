"""
582. Word Break II
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
Example 1:

Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
Example 2:

Input："a"，[]
Output：[]
Explanation：dict is null.
"""


class Solution:
    def wordBreak(self, s, wordDict):
        return self.helper(s, 0, wordDict, {})

    def helper(self, s, start, wordDict, memo):
        if start == len(s):
            return []
        if start in memo:
            return memo[start]
        result = []
        for i in range(start + 1, len(s)):
            if s[start:i] in wordDict:
                strings_after = self.helper(s, i, wordDict, memo)
                if strings_after:
                    for j in strings_after:
                        result.append(s[start:i] + " " + j)
        if s[start:] in wordDict:
            result.append(s[start:])
        memo[start] = result
        return result


if __name__ == '__main__':
    print(Solution().wordBreak('a', []))