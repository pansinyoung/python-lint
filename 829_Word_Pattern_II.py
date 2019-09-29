"""
829. Word Pattern II
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

Example
Example 1

Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
Example 2

Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"
Example 3

Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false
Notice
You may assume both pattern and str contains only lowercase letters.
"""
import collections


class Solution:
    def wordPatternMatch(self, pattern, s):
        return self.helper(pattern, s, {}, set())

    def helper(self, pattern, s, mapping, used):
        if not pattern:
            return not s

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if s.startswith(word):
                return self.helper(pattern[1:], s[len(word):], mapping, used)
            else:
                return False

        for i in range(len(s)):
            word = s[:i + 1]
            if word in used:
                continue
            used.add(word)
            mapping[char] = word
            if self.helper(pattern[1:], s[i + 1:], mapping, used):
                return True
            used.remove(word)
            del mapping[char]

        return False


def main():
    s = Solution()
    print(s.wordPatternMatch('aabb', 'aabb'))


if __name__ == '__main__':
    main()
