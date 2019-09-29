"""
17. Subsets
Given a set of distinct integers, return all possible subsets.

Example
Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Challenge
Can you do it in both recursively and iteratively?

Notice
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
"""
import collections

class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        nums.sort()

        # return self.traverse(nums)

        #recursive
        result = []
        self.recursive(nums, 0, [], result)
        return result

    def traverse(self, nums):
        l = len(nums)
        result = []
        queue = collections.deque()
        queue.append(([], 0))
        while queue:
            cur = queue.pop()
            if cur[1] == l:
                result.append(cur[0])
                continue
            queue.append((cur[0], cur[1] + 1))
            queue.append((cur[0] + [nums[cur[1]]], cur[1] + 1))
        return result

    def recursive(self, nums, i, prev, result):
        if i == len(nums):
            result.append(prev)
            return
        self.recursive(nums, i + 1, prev + [nums[i]], result)
        self.recursive(nums, i + 1, prev, result)

def main():
    s = Solution()
    print(s.subsets([1, 2, 3]))


if __name__ == '__main__':
    main()
