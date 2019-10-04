"""
461. Kth Smallest Numbers in Unsorted Array
Find the kth smallest number in an unsorted integer array.

Example
Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:

Input: [1, 1, 1], k = 2
Output: 1
Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
"""


class Solution:
    def kthSmallest(self, k, nums):
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if right >= k and start <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k and left <= end:
            return self.quickSelect(nums, left, end, k)
        else:
            return nums[k]


def main():
    s = Solution()
    numbers = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(numbers))


if __name__ == '__main__':
    main()
