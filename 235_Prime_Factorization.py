"""
235. Prime Factorization
 Prime factorize a given integer.

Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
Notice
You should sort the factors in ascending order.
"""
from typing import List


class Solution:
    def primeFactorization(self, num):
        top = num ** 0.5 + 1
        result = []
        for i in range(2, top):
            while num % i == 0:
                result.append(i)
                num = num // i
        if num > 1:
            result.append(num)
        return result



def main():
    s = Solution()
    x = [1, 4, 6]
    n = 5

    print(s.closestNumber(x, n))


if __name__ == "__main__":
    main()
