"""
414. Divide Two Integers
Divide two integers without using multiplication, division and mod operator.

If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647

The integer division should truncate toward zero.

Example
Example 1:

Input: dividend = 0, divisor = 1
Output: 0
Example 2:

Input: dividend = 100, divisor = 9
Output: 11
"""
import sys


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = sys.maxsize
        if divisor == 0:
            return MAX
        if dividend == 0:
            return 0
        positive = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        cur = 1
        cur_divisor = divisor
        result = 0
        while dividend >= divisor:
            cur = cur << 1
            cur_divisor = cur_divisor << 1
            if cur_divisor > dividend:
                cur = cur >> 1
                cur_divisor = cur_divisor >> 1
                dividend = dividend - cur_divisor
                result += cur
                cur = 1
                cur_divisor = divisor
        if not positive:
            result = -result
        return result if result < MAX else MAX



def main():
    s = Solution()
    source = -2147483648
    target = -1
    print(s.divide(source, target))


if __name__ == "__main__":
    main()
