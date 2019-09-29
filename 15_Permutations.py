"""
15. Permutations
Given a list of numbers, return all possible permutations.

Example
Example 1:

Input: [1]
Output:
[
  [1]
]
Example 2:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
Do it without recursion.

Notice
You can assume that there is no duplicate numbers in the list.
"""
import collections

class Solution:
    def permute(self, nums):
        # results = []
        # self.recursive(nums, [], results)
        # return results

        return self.traverse(nums)

    def traverse(self, nums):
        queue = collections.deque()
        queue.append((nums, []))
        result = []
        while queue:
            cur = queue.pop()
            if not cur[0]:
                result.append(cur[1])
                continue
            for i in range(len(cur[0])):
                queue.append((cur[0][:i] + cur[0][i + 1:], cur[1] + [cur[0][i]]))
        return result

    def recursive(self, nums, prev, result):
        if not nums:
            result.append(prev)
            return
        for i in range(len(nums)):
            self.recursive(nums[:i] + nums[i + 1:], prev + [nums[i]], result)

def main():
    s = Solution()
    print(s.permute([1, 2, 3]))


if __name__ == '__main__':
    main()
