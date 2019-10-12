"""
634. Word Squares
Given a set of words without duplicates, find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Example
Example 1:

Input:
["area","lead","wall","lady","ball"]
Output:
[["wall","area","lead","lady"],["ball","area","lead","lady"]]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]
Output:
 [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
Notice
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
"""


class Solution:
    def wordSquares(self, words):
        if not words:
            return []
        n = len(words[0])
        prefix_dicts = [{} for _ in range(n + 1)]
        prefix_dicts[0] = {'': words}
        for w in words:
            for i in range(1, n):
                if w[:i] not in prefix_dicts[i]:
                    prefix_dicts[i][w[:i]] = []
                prefix_dicts[i][w[:i]].append(w)
        result = []
        self.helper(prefix_dicts, [], 0, n, result)
        return result

    def helper(self, prefix_dict, prev, row, n, result):
        if row == n:
            result.append(prev[:])
            return
        cur = ''.join([prev[i][row] for i in range(row)])
        if cur not in prefix_dict[row]:
            return
        for w in prefix_dict[row][cur]:
            prev.append(w)
            self.helper(prefix_dict, prev, row + 1, n, result)
            prev.pop()


if __name__ == '__main__':
    print(Solution().wordSquares(["area", "lead", "wall", "lady", "ball"]))
