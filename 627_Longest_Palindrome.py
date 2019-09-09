"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
Notice
Assume the length of given string will not exceed 1010.
"""


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        occurrence = {}
        result = 0
        odd_occurred = False
        for c in s:
            if c not in occurrence.keys():
                occurrence[c] = 1
            else:
                occurrence[c] += 1

        for v in occurrence.values():
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                odd_occurred = True
        return (result + 1) if odd_occurred else result

def main():
    s = Solution()
    test1 = ''
    test2 = 'asdf'
    test3 = 'NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy'
    test4 = 'dbcbaccdccbdbcabbcbcadaadcacaaabaabadbdcdaccbccabbbdcadacbcdbabadcdcdaddbabbabdcacbaddadcbaccdcdcdacabababdababdbadadabdacbdddcdbbabcabcbaabbcacddddaadaabbcdccddabcadcaaccbbdbcbbbdaabdadbaaaddcbabdbbabcaabdbbcaabdbcbcabababddcacacbadabdacddccaccaacdacddcbbadcabcddacaadddbbaadacddbdacdcd'
    print(test1, s.longestPalindrome(test1))
    print(test2, s.longestPalindrome(test2))
    print(test3, s.longestPalindrome(test3))
    print(test4, s.longestPalindrome(test4))


if __name__ == '__main__':
    main()
