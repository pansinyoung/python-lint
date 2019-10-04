"""
148. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example
Example 1

Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place
Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

Notice
You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).
"""


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors(self, nums):
        last_end = -1
        for x in range(3):
            i = last_end + 1
            j = len(nums) - 1
            while i < len(nums):
                while i < len(nums) and nums[i] == x:
                    last_end = i
                    i += 1
                if i == len(nums):
                    break
                while j > i and nums[j] != x:
                    j -= 1
                if j <= i:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                last_end = i
                i += 1
                j -= 1


def main():
    s = Solution()
    colors = [1, 0, 1, 2]
    s.sortColors(colors)
    print(colors)


if __name__ == '__main__':
    main()
