"""
32. Minimum Window Substring
Given two strings source and target. Return the minimum substring of source which contains each char of target.

Example
Example 1:

Input: source = "abc", target = "ac"
Output: "abc"
Example 2:

Input: source = "adobecodebanc", target = "abc"
Output: "banc"
Explanation: "banc" is the minimum substring of source string which contains each char of target "abc".
Example 3:

Input: source = "abc", target = "aa"
Output: ""
Explanation: No substring contains two 'a'.
Challenge
O(n) time

Notice
If there is no answer, return "".
You are guaranteed that the answer is unique.
target may contain duplicate char, while the answer need to contain at least the same number of that char.
"""
from typing import Dict


class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def get_string_dict(self, s: str) -> Dict:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        return result

    def check_if_valid(self, dic_s: Dict, dic_t: Dict) -> bool:
        for k in dic_t:
            if k not in dic_s or dic_t[k] > dic_s[k]:
                return False
        return True

    def minWindow(self, source: str, target: str) -> str:
        if not source or not target:
            return ""
        dic_source = self.get_string_dict(source)
        dic_target = self.get_string_dict(target)
        if not self.check_if_valid(dic_source, dic_target):
            return ""
        n = len(source)
        result = (0, n)
        for i in range(n - len(target) + 1):
            if source[i] not in dic_target:
                continue
            if not self.check_if_valid(dic_source, dic_target):
                break
            j = n
            while i + len(target) - 1 < j <= n:
                if source[j - 1] not in dic_target:
                    j -= 1
                    continue
                dic_source[source[j - 1]] -= 1
                if not self.check_if_valid(dic_source, dic_target):
                    if j - i < result[1] - result[0]:
                        result = (i, j)
                    while j <= n:
                        if source[j - 1] in dic_target:
                            dic_source[source[j - 1]] += 1
                        j += 1
                    break
                j -= 1
            dic_source[source[i]] -= 1
        return source[result[0]: result[1]]


def main():
    s = Solution()
    source = "adobecodebanc"
    target = "abc"
    print(s.minWindow(source, target))


if __name__ == '__main__':
    main()
