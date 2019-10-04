"""
59. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Example
Example 1:

Input:[2,7,11,15],3
Output:20
Explanation:
2+7+11=20
Example 2:

Input:[-1,2,1,-4],1
Output:2
Explanation:
-1+2+1=2
Challenge
O(n^2) time, O(1) extra space

Notice
You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, numbers, target):
        numbers.sort()
        result = sum(numbers[:3])
        for i in range(2, len(numbers)):
            cur = self.twoSumClosest(numbers, 0, i - 1, target)
            result = cur if abs(cur - target) < abs(result - target) else result
        return result

    def twoSumClosest(self, numbers, start, end, target):
        left, right = start, end
        result = sum([numbers[left], numbers[right], numbers[end + 1]])
        while left < right:
            cur = sum([numbers[left], numbers[right], numbers[end + 1]])
            if cur == target:
                return cur
            if abs(target - cur) < abs(target - result):
                result = cur
            if cur > target:
                right -= 1
            else:
                left += 1
        return result


def main():
    s = Solution()
    numbers = [-1, 2, 1, -4]
    target = 1
    print(s.threeSumClosest(numbers, target))


if __name__ == '__main__':
    main()
