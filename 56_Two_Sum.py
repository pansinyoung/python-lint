"""
56. Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

Example
Example1:
numbers=[2, 7, 11, 15], target=9
return [0, 1]
Example2:
numbers=[15, 2, 7, 11], target=9
return [1, 2]
Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
Notice
You may assume that each input would have exactly one solution
"""


class TwoSum:
    def twoSum(self, numbers, target):
        dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                return [dict[target - numbers[i]], i]
            dict[numbers[i]] = i
        return []

def main():
    s = Solution()
    source = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 1
    print(s.searchMatrix(source, target))


if __name__ == "__main__":
    main()
