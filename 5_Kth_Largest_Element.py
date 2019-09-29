"""
5. Kth Largest Element
Find K-th largest element in an array.

Example
Example 1:

Input:
n = 1, nums = [1,3,4,2]
Output:
4
Example 2:

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4
Challenge
O(n) time, O(1) extra memory.

Notice
You can swap elements in the array
"""


class Solution:
    def kthLargestElement(self, n, nums):
        if not nums or n > len(nums) or n < 1:
            return -1
        if len(nums) == 1:
            return nums[0]
        pivot = nums[len(nums) // 2]
        upper = []
        equal = []
        lower = []
        for i in nums:
            if i > pivot:
                upper.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                lower.append(i)
        if n <= len(upper):
            return self.kthLargestElement(n, upper)
        elif n <= len(upper) + len(equal):
            return pivot
        else:
            return self.kthLargestElement(n - len(upper) - len(equal), lower)


def main():
    s = Solution()
    numbers = [9,3,2,4,8]
    print(s.kthLargestElement(3, numbers))


if __name__ == '__main__':
    main()
