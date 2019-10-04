"""
10. String Permutation II
Given a string, find all permutations of it without duplicates.

Example
Example 1:

Input: "abb"
Output:
["abb", "bab", "bba"]
Example 2:

Input: "aabb"
Output:
["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""


class Solution:
    def stringPermutation2(self, str):
        char_map = {}
        for c in str:
            char_map[c] = char_map.get(c, 0) + 1
        result = []
        self.helper(char_map, "", result)
        return result

    def helper(self, char_map, prev, result):
        if not char_map or sum(char_map.values()) == 0:
            result.append(prev)
            return
        for c in char_map:
            if char_map[c] == 0:
                continue
            char_map[c] -= 1
            self.helper(char_map, prev + c, result)
            char_map[c] += 1


if __name__ == '__main__':
    print(Solution().stringPermutation2('abb'))