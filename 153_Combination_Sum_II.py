"""
153. Combination Sum II
Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.

Example
Example 1:

Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Example 2:

Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.
Notice
Each number in num can only be used once in one combination.
All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, num, target):
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
            while next_non_dup < len(num) and num[i] == num[next_non_dup]:
                next_non_dup += 1
            cur = list(prev)
            cur_sum = prev_sum
            while i < next_non_dup:
                cur_sum = cur_sum + num[i]
                cur = cur + [num[i]]
                if cur_sum == target:
                    result.append(cur)
                    break
                if cur_sum < target:
                    self.helper(num, next_non_dup, cur, target, result)
                    i += 1
                else:
                    break
            self.helper(num, next_non_dup, prev, target, result)



def main():
    s = Solution()
    num = [1, 1, 1, 2, 2, 2, 2, 3, 3]
    target = 7
    print(s.combinationSum2(num, target))


if __name__ == '__main__':
    main()
