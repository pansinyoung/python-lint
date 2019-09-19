"""
624. Remove Substrings
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

Example
Example 1:

Input:
"ccdaabcdbb"
["ab","cd"]
Output:
2
Explanation:
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
Example 2:

Input:
"abcabd"
["ab","abcd"]
Output:
0
Explanation:
abcabd -> abcd -> "" (length = 0)
"""
from typing import Set
from collections import deque


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s: str, dict: Set[str]):
        if not s:
            return 0
        result = len(s)
        visited = set()
        visited.add(s)
        queue = deque()
        queue.append(s)
        while queue:
            cur = queue.popleft()
            new = False
            for d in dict:
                for x in self.replace_first_occurance(cur, d):
                    if not x:
                        return 0
                    if x != cur and x not in visited:
                        queue.append(x)
                        visited.add(x)
                        new = True
            if not new:
                result = min(result, len(cur))
        return result

    def replace_first_occurance(self, s: str, tar: str) -> Set[str]:
        result = set()
        start = 0
        i = s.find(tar, start)
        while i >= 0:
            result.add(s[:i] + (s[i + len(tar):] if i + len(tar) <= len(s) else ''))
            start = i + 1
            i = s.find(tar, start)
        return result

def main():
    s = Solution()
    source = 'ccdaabcdbb'
    dict = ["ab", "cd"]
    print(s.minLength(source, dict))


if __name__ == '__main__':
    main()
