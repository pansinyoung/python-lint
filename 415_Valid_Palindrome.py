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
        i = 0
        j = len(s) - 1
        while i < len(s) and not s[i].isalnum():
            i += 1
        while j >= 0 and not s[j].isalnum():
            j -= 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1

        return True


def main():
    a = 'A man, a plan, a canal: Panama'
    b = ''
    c = 'race a car'
    d = '1a2'
    e = '.;'
    s = Solution()
    print(s.isPalindrome(a))
    print(s.isPalindrome(b))
    print(s.isPalindrome(c))
    print(s.isPalindrome(d))
    print(s.isPalindrome(e))


if __name__ == '__main__':
    main()
