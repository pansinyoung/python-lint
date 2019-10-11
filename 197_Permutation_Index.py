"""
197. Permutation Index
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example
Example 1:

Input:[1,2,4]
Output:1
Example 2:

Input:[3,2,1]
Output:6
"""


class Solution:
    def permutationIndex(self, A):
        num_rank = {}
        n = len(A)
        for i in range(n):
            cur_rank = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    cur_rank += 1
            num_rank[A[i]] = cur_rank
        i = n - 2
        result = 1
        factor = 1
        while i >= 0:
            result = num_rank[A[i]] * factor + result
            factor *= n - i
            i -= 1
        return result


if __name__ == '__main__':
    print(Solution().permutationIndex([11]))
