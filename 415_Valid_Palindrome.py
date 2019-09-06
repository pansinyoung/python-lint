"""
415. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"
Challenge
O(n) time without extra memory.

Notice
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s: str):
        s = s.lower()
        s = ''.join(c if c.isalnum() else '' for c in s)
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True


def main():
    a = 'A man, a plan, a canal: Panama'
    b = ''
    c = 'race a car'
    d = '1a2'
    s = Solution()
    print(s.isPalindrome(d))


if __name__ == '__main__':
    main()
