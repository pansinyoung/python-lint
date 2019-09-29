"""
18. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Example
Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Challenge
Can you do it in both recursively and iteratively?

Notice
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.
"""
import collections

class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        nums.sort()

        return self.traverse(nums)

        # #recursive
        # result = []
        # self.recursive(nums, 0, [], result)
        # return result

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
            next_non_dup = cur[1]
            while next_non_dup < l and nums[next_non_dup] == nums[cur[1]]:
                next_non_dup += 1
            new_list = list(cur[0])
            new_I = cur[1]
            while new_I < next_non_dup:
                new_list += [nums[new_I]]
                queue.append((list(new_list), next_non_dup))
                new_I += 1
            queue.append((cur[0], next_non_dup))
        return result

    def recursive(self, nums, i, prev, result):
        if i == len(nums):
            result.append(prev)
            return
        next_non_dup = i
        while next_non_dup < len(nums) and nums[next_non_dup] == nums[i]:
            next_non_dup += 1
        cur = list(prev)
        while i < next_non_dup:
            cur += [nums[i]]
            self.recursive(nums, next_non_dup, list(cur), result)
            i += 1
        self.recursive(nums, next_non_dup, prev, result)

def main():
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))


if __name__ == '__main__':
    main()
