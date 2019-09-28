"""
143. Sort Colors II
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Example1

Input:
[3,2,2,1,4]
4
Output:
[1,2,2,3,4]
Example2

Input:
[2,1,1,2,2]
2
Output:
[1,1,2,2,2]
Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?

Notice
You are not suppose to use the library's sort function for this problem.
k <= n
"""


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        last_end = -1
        for x in range(1, k + 1):
            i = last_end + 1
            j = len(colors) - 1
            while i < len(colors):
                print(colors)
                while i < len(colors) and colors[i] == x:
                    last_end = i
                    i += 1
                if i == len(colors):
                    break
                while j > i and colors[j] != x:
                    j -= 1
                if j <= i:
                    break
                temp = colors[j]
                colors[j] = colors[i]
                colors[i] = temp
                last_end = i
                i += 1
                j -= 1


def main():
    s = Solution()
    colors = [3, 2, 1, 4]
    k = 4
    s.sortColors2(colors, 2)
    print(colors)


if __name__ == '__main__':
    main()
