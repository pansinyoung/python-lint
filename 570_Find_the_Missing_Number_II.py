"""
570. Find the Missing Number II
中文English
Giving a string with number from 1-n in random order, but miss 1 number.Find that number.

Example
Example1

Input: n = 20 and str = 19201234567891011121314151618
Output: 17
Explanation:
19'20'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'16'18
Example2

Input: n = 6 and str = 56412
Output: 3
Explanation:
5'6'4'1'2
Notice
n <= 30
Data guarantees have only one solution
"""

class Solution:
    def findMissing2(self, n, s):
        result_set = set([str(_) for _ in range(1, n + 1)])
        return self.helper(n, s, 0, result_set)

    def helper(self, n, s, start, result_set):
        print(start, result_set)
        if start >= len(s):
            return int(result_set.pop()) if len(result_set) == 1 else None
        if s[start] == '0':
            return None
        i, cur = 1, s[start]
        while start + i <= len(s) and int(cur) <= n:
            if cur in result_set:
                result_set.remove(cur)
                next = self.helper(n, s, start + i, result_set)
                if next is not None:
                    return next
                result_set.add(cur)
            i += 1
            cur = s[start: start + i]
        return None


def main():
    print(Solution().findMissing2(20, '19201234567891011121314151618'))


if __name__ == "__main__":
    main()