"""
198. Permutation Index II
Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example
Example 1:

Input :[1,4,2,2]
Output:3
Example 2:

Input :[1,6,5,3,1]
Output:24
"""


class Solution:
    def permutationIndexII(self, A):
        if len(A) <= 1:
            return 1
        n = len(A)
        result = 1
        i = n - 1
        factor = 1
        divider = 1
        counter = {i: 0 for i in A}
        while i >= 0:
            counter[A[i]] += 1
            divider *= counter[A[i]]
            rank = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    rank += 1

            result = (factor/divider) * rank + result
            factor *= n - i
            i -= 1
        return int(result)


if __name__ == '__main__':
    print(Solution().permutationIndexII([3, 2, 2, 1, 1]))
