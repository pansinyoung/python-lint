"""
152. Combinations
Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n.

Example
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Example 2:

Input: n = 4, k = 1
Output: [[1],[2],[3],[4]]
Notice
You can return all combinations in any order, but numbers in a combination should be in ascending order.
"""


class Solution:
    def combine(self, n, k):
        result = []
        self.helper(n, [], result, k)
        return result

    def helper(self, n, prev, result, k):
        if len(prev) == k:
            result.append(prev[:])
            return
        for i in range(prev[-1] + 1 if prev else 1, n + 1):
            prev.append(i)
            self.helper(n, prev, result, k)
            prev.pop()


if __name__ == '__main__':
    print(Solution().combine(4, 2))