"""
209. First Unique Character in a String
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

Example
Example 1:
	Input: "abaccdeff"
	Output:  'b'

	Explanation:
	There is only one 'b' and it is the first one.
Example 2:
	Input: "aabccd"
	Output:  'b'

	Explanation:
	'b' is the first one.
"""
import collections


class Solution:
    def firstUniqChar(self, str):
        counter = {}
        for c in str:
            counter[c] = counter[c] + 1 if c in counter else 1
        for c in str:
            if counter[c] == 1:
                return c
