"""
428. Pow(x, n)
中文English
Implement pow(x, n). (n is an integer.)

Example
Example 1:

Input: x = 9.88023, n = 3
Output: 964.498
Example 2:

Input: x = 2.1, n = 3
Output: 9.261
Example 3:

Input: x = 1, n = 0
Output: 1
Challenge
O(logn) time

Notice
You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.
"""


class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1 or n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        if n % 2 == 1:
            return self.myPow(x, (n - 1) // 2) ** 2 * x
        else:
            return self.myPow(x, n // 2) ** 2


def main():
    s = Solution()
    x = 8.84372
    n = -5

    print(s.myPow(x, n))


if __name__ == "__main__":
    main()
