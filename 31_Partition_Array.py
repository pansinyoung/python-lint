"""
31. Partition Array
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
Challenge
Can you partition the array in-place and in O(n)?

Notice
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
"""


class Solution:
    def partitionArray(self, nums, k):
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] < k:
                i += 1
            if i >= j:
                return i
            while j >= i and nums[j] >= k:
                j -= 1
            if j <= i:
                return i
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return i



def main():
    s = Solution()
    numbers = [3,2,2,1]
    print(s.partitionArray(numbers, 0))


if __name__ == '__main__':
    main()
