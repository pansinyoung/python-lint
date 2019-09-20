"""
892. Alien Dictionary
中文English
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rtff" ,we can get 'e'<'r'
So return "wertf"

Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
Notice
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
"""
from typing import List


class Solution:

    def compare_two_words(self, s: str, t: str) -> tuple:
        l = min(len(s), len(t))
        for i in range(l):
            if s[i] != t[i]:
                return ord(s[i]) - 97, ord(t[i]) - 97
        return -1, -1

    def alienOrder(self, words: List[str]) -> str:
        if len(words) < 1:
            return ''
        degrees = [0] * 26
        edges = [[] for _ in range(26)]
        visited = set()
        chars = set()
        for i in range(len(words)):
            for c in words[i]:
                chars.add(ord(c) - 97)
            for j in range(i + 1, len(words)):
                cur = self.compare_two_words(words[i], words[j])
                if cur[0] != -1 and cur not in visited:
                    visited.add(cur)
                    degrees[cur[1]] += 1
                    edges[cur[0]].append(cur[1])
        floater_chars = []
        for c in chars:
            if degrees[c] == 0 and not edges[c]:
                floater_chars.append(c)
        for c in floater_chars:
            chars.remove(c)
        result = []
        while chars:
            cur = []
            found = False
            for c in chars:
                if degrees[c] == 0 and c not in result:
                    found = True
                    cur.append(c)
            if not found:
                break
            for c in cur:
                for i in edges[c]:
                    degrees[i] -= 1
                chars.remove(c)
            cur.sort()
            result += cur
        for c in floater_chars:
            i = 0
            while i < len(result):
                if c < result[i]:
                    break
                i += 1
            result.insert(i, c)
        return '' if chars else ''.join(chr(i + 97) for i in result)



def main():
    s = Solution()
    list = ["zw", "zy"]
    print(s.alienOrder(list))


if __name__ == '__main__':
    main()
