"""
425. Letter Combinations of a Phone Number
Given a digit string excluded '0' and '1', return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

1	2
ABC	3
DEF
4
GHI	5
JKL	6
MNO
7
PQRS	8
TUV	9
WXYZ
Example
Example 1:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation:
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'
Example 2:

Input: "5"
Output: ["j", "k", "l"]
Notice
Although the answer above is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        num_chars_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        self.helper(digits, 0, "", result, num_chars_dict)
        return result

    def helper(self, s, i, prev, result, num_chars_dict):
        if i == len(s):
            result.append(prev)
            return
        for c in num_chars_dict[s[i]]:
            self.helper(s, i + 1, prev + c, result, num_chars_dict)



def main():
    s = Solution()
    t = '23'
    print(s.letterCombinations(t))

if __name__ == '__main__':
    main()
