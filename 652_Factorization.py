"""
652. Factorization
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Example
Example1

Input: 8
Output: [[2,2,2],[2,4]]
Explanation:
8 = 2 x 2 x 2 = 2 x 4
Example2

Input: 1
Output: []
Notice
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.
"""
import math


class Solution:
    def getFactors(self, n):
        result = []
        self.helper(n, 2, [], result)
        return result

    def helper(self, n, start, prev, result):
        if n <= 1:
            if prev and len(prev) > 1:
                result.append(prev[:])
            return
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prev.append(i)
                self.helper(n // i, i, prev, result)
                prev.pop()
        prev.append(n)
        self.helper(1, n, prev, result)
        prev.pop()


def main():
    print(Solution().getFactors(100))


if __name__ == "__main__":
    main()
