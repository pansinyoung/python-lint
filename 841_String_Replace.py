"""
841. String Replace
Given two identical-sized string array A, B and a string S. All substrings A appearing in S are replaced by B.(Notice:
From left to right, it must be replaced if it can be replaced. If there are multiple alternatives, replace longer
priorities. After the replacement of the characters can't be replaced again.)

Example
Example 1

Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "ababa"

Output: "cccba"
Explanation: In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is longer,
we replace "aba" with "ccc".
Example 2

Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "aaaaa"

Output: "aaaaa"
Explanation: S does not contain strings in A, so no replacement is done.
Example 3

Input:
A = ["cd","dab","ab"]
B = ["cc","aaa","dd"]
S = "cdab"

Output: "ccdd"
Explanation: From left to right, you can find the "cd" can be replaced at first, so after the replacement becomes
"ccab", then you can find "ab" can be replaced, so the string after the replacement is "ccdd".

Notice
The size of each string array does not exceed 100, the total string length does not exceed 50000.
The lengths of A [i] and B [i] are equal.
The length of S does not exceed 50000.
All characters are lowercase letters.
We guarantee that the A array does not have the same string
"""
from typing import List


class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a: List[str], b: List[str], s: str) -> str:
        if not (a and b and str):
            return str

        seed = 33
        mod = 1000007
        a_hash_values = []
        s_hash_values = []
        base_hash = []



def main():
    s = Solution()
    test = 'abcdefg'
    print(s.RotateString2(test, 3, 1))


if __name__ == '__main__':
    main()
