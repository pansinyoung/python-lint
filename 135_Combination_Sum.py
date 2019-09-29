"""
135. Combination Sum
Given a set of candidtate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Example
Example 1:

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Example 2:

Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
Notice
All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum(self, num, target):
        num.sort()
        result = []
        self.helper(num, 0, [], target, result)
        return result

    def helper(self, num, i, prev, target, result):
        if i == len(num):
            return
        prev_sum = sum(prev)
        if prev_sum + num[i] == target:
            result.append(prev + [num[i]])
        elif prev_sum + num[i] < target:
            next_non_dup = i
            while next_non_dup < len(num) and num[next_non_dup] == num[i]:
                next_non_dup += 1
            cur = list(prev)
            cur_sum = prev_sum
            while cur_sum < target:
                self.helper(num, next_non_dup, cur, target, result)
                cur += [num[i]]
                cur_sum += num[i]
                if cur_sum == target:
                    result.append(cur)
                    break



def main():
    s = Solution()
    num = [2, 2, 3, 7]
    target = 5
    print(s.combinationSum(num, target))


if __name__ == '__main__':
    main()
