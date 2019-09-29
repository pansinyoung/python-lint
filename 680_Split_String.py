"""
680. Split String
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

Example
Example1

Input: "123"
Output: [["1","2","3"],["12","3"],["1","23"]]
Example2

Input: "12345"
Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""


class Solution:
    def splitString(self, s):
        if not s:
            return [[]]
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s, i, prev, result):
        if i == len(s):
            result.append(prev)
            return
        if i == len(s) - 1:
            result.append(prev + [s[i:]])
            return
        self.helper(s, i + 1, prev + [s[i:i + 1]], result)
        self.helper(s, i + 2, prev + [s[i:i + 2]], result)


def main():
    s = Solution()
    t = '12345'
    print(s.splitString(t))

if __name__ == '__main__':
    main()
