"""
604. Window Sum
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example
Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
"""


class Solution:
    def winSum(self, nums, k):
        if k > len(nums) or k == 0:
            return []
        i, j, sum, result = 0, k - 1, 0, []
        for i in range(k):
            sum += nums[i]
        i = 0
        result.append(sum)
        while j < len(nums) - 1:
            j += 1
            sum += nums[j] - nums[i]
            i += 1
            result.append(sum)
        return result


def main():
    s = Solution()
    numbers = [9,3,2,4,8]
    print(s.kthLargestElement(3, numbers))


if __name__ == '__main__':
    main()
