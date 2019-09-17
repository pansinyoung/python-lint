"""
140. Fast Power
中文English
Calculate the an % b where a, b and n are all 32bit non-negative integers.

Example
For 2^31 % 3 = 2

For 1001000 % 1000 = 0

Challenge
O(logn)
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a: int, b: int, n: int) -> int:
        if b == 0:
            return -1
        if a == 0:
            return 0
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        if n % 2 == 1:
            return ((self.fastPower(a, b, n // 2) ** 2) * a) % b
        else:
            return (self.fastPower(a, b, n // 2) ** 2) % b



def main():
    s = Solution()
    a = 3
    b = 1
    n = 0

    print(s.fastPower(a, b, n))


if __name__ == '__main__':
    main()
