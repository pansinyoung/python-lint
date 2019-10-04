"""
382. Triangle Count
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

Example
Example 1:

Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6),
         (3, 6, 7),
         (4, 6, 7)
Example 2:

Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle.
So the answer is C(3, 4) = 4
"""


class Solution:
    def triangleCount(self, S):
        result = 0
        if len(S) < 3:
            return 0
        for i in range(2, len(S)):
            result += self.twoSum2(S, 0, i - 1, S[i])
        return result

    def twoSum2(self, nums, left, right, target):
        nums.sort()
        result, start, end = 0, left, right
        while end > start:
            while nums[start] + nums[end] <= target:
                start += 1
            if start < end:
                result += end - start
            end -= 1
        return result


def main():
    s = Solution()
    nums = [4, 4, 4, 4]
    target = 1
    print(s.triangleCount(nums))


if __name__ == "__main__":
    main()
