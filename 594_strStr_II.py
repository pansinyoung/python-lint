"""
594. strStr II
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

Example
Example 1:

Input：source = "abcdef"， target = "bcd"
Output：1
Explanation：
The position of the first occurrence of a string is 1.
Example 2:

Input：source = "abcde"， target = "e"
Output：4
Explanation：
The position of the first occurrence of a string is 4.
"""


class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source: str, target: str) -> int:
        if source is None or target is None:
            return -1
        if len(target) == 0:
            return 0
        if len(source) < len(target):
            return -1
        seed = 33
        mod = 10007
        tar_hash = 0
        for c in target:
            tar_hash = (tar_hash * seed + ord(c) - 96) % mod

        tar_len = len(target)
        base = 33**(tar_len - 1) % mod
        sour_hash = 0
        for i in range(tar_len):
            sour_hash = (sour_hash * seed + (ord(source[i]) - 96)) % mod
        if sour_hash == tar_hash and source[:tar_len] == target:
            return 0
        for i in range(1, len(source) - len(target) + 1):
            sour_hash = ((sour_hash - (ord(source[i - 1]) - 96) * base % mod) * seed + (ord(source[i + tar_len - 1]) - 96)) % mod
            if sour_hash == tar_hash:
                return i
        return -1

def main():
    s = Solution()
    source = 'abcdef'
    target = 'ef'
    print(s.strStr2(source, target))


if __name__ == '__main__':
    main()
