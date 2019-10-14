"""
1629. Find the nearest store
There are some stores and houses on a street. Please find the nearest store to each house.

You are given two array represent the location of the stores and houses.

Return an array with the location of the nearest store to each house. If there are two stores that are the same distance from the house return the left one.

Tips:
1. There are multiple stores and houses in the same location. And the locations in array are disordered.
2. The array of location must not be empty.
Example
Example 1:

stores: [4,7,8,1,6,6,2]
houses: [1, 8, 5]
return: [1, 8, 4]

Input:
4 7 8 1 6 6 2
1 8 5
Output:
1 8 4
Example 2:

stores: [2,3,5,5,6,10]
houses: [4,11,7]
return: [3,10,6]

Input:
2 3 5 5 6 10
4 11 7
Output:
3 10 6
"""


class Solution:
    def findNearestStore(self, stores, houses):
        stores.sort()
        ans = [-1 for _ in houses]
        for i in range(len(houses)):
            left, right = 0, len(stores) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if stores[mid] >= houses[i]:
                    right = mid
                else:
                    left = mid
            if abs(stores[right] - houses[i]) < abs(stores[left] - houses[i]):
                ans[i] = stores[right]
            else:
                ans[i] = stores[left]
        return ans


if __name__ == '__main__':
    print(Solution().findNearestStore([4, 7, 8, 1, 6, 6, 2], [1, 8, 5]))
