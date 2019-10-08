"""
683. Word Break III
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 0
Notice
Ignore case
"""


class Solution:

    def wordBreak3(self, s, dict):
        return self.helper(s.lower(), 0, [d.lower() for d in dict], {})

    def helper(self, s, start, dict, memo):
        if s[start:] in memo:
            return memo[s[start:]]
        if start == len(s):
            return 1
        result = 0
        for i in range(start + 1, len(s) + 1):
            if s[start:i] in dict:
                result += self.helper(s, i, dict, memo)
        memo[s[start:]] = result
        return result


if __name__ == '__main__':
    print(Solution().wordBreak3('a', []))
