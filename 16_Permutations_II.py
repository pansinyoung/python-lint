"""
16. Permutations II
Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
Example 1:

Input: [1,1]
Output:
[
  [1,1]
]
Example 2:

Input: [1,2,2]
Output:
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!
"""


class Solution:
    def permuteUnique(self, nums):
        result = []
        num_map = {}
        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1
        self.helper(num_map, [], result, len(nums))
        return result

    def helper(self, num_map, prev, result, k):
        if len(prev) == k:
            result.append(prev[:])
            return
        for n in num_map:
            if num_map[n] == 0:
                continue
            num_map[n] -= 1
            prev.append(n)
            self.helper(num_map, prev, result, k)
            prev.pop()
            num_map[n] += 1


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1]))