"""
124. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example
Example 1

Input : [100, 4, 200, 1, 3, 2]
Output : 4
Explanation : The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4
Clarification
Your algorithm should run in O(n) complexity.
"""


class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        if not num:
            return 0
        if len(num) <= 1:
            return len(num)
        num_set = set(num)
        result = 0
        for n in num:
            if n not in num_set:
                continue
            cur = 1
            i = 1
            while n - i in num_set:
                num_set.remove(n - i)
                cur += 1
                i -= 1

            i = 1
            while n + 1 in num_set:
                num_set.remove(n + i)
                cur += 1
                i += 1
            result = max(result, cur)
            num_set.remove(n)
        return result
