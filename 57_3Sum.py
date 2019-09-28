"""
57. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
Example 1:

Input:[2,7,11,15]
Output:[]
Example 2:

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
Notice
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
"""


class Solution:

    def threeSum(self, numbers):
        numbers.sort()
        result = []
        for i in range(len(numbers) - 1):
            if i and numbers[i - 1] == numbers[i]:
                continue
            self.twoSum(numbers, i + 1, len(numbers) - 1, -numbers[i], result)
        return result

    def twoSum(self, numbers, start, end, target, result):
        while start < end:
            if numbers[start] + numbers[end] == target:
                result.append([-target, numbers[start], numbers[end]])
                start += 1
                end -= 1
                while start < end and numbers[start - 1] == numbers[start]:
                    start += 1
                while start < end and numbers[end + 1] == end:
                    end -= 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1


def main():
    s = Solution()
    numbers = [-1,0,1,2,-1,-4]
    print(s.threeSum(numbers))


if __name__ == '__main__':
    main()
