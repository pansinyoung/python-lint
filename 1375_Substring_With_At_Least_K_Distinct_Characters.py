"""
1375. Substring With At Least K Distinct Characters
Given a string S with only lowercase characters.

Return the number of substrings that contains at least k distinct characters.

Example
Example 1:

Input: S = "abcabcabca", k = 4
Output: 0
Explanation: There are only three distinct characters in the string.
Example 2:

Input: S = "abcabcabcabc", k = 3
Output: 55
Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
    For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
    There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
    ...
    There is 1 substring whose length is 12, "abcabcabcabc"
    So the answer is 1 + 2 + ... + 10 = 55.
Notice
10 ≤ length(S) ≤ 1,000,000
1 ≤ k ≤ 26
"""


class Solution:
    def kDistinctCharacters(self, s, k):
        result = 0
        left, count = 0, {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while left <= right and len(count) >= k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            if len(count) == k - 1:
                result += left
        return result


def main():
    s = Solution()
    t = 'veunvywzrejbyawhzkwzraafgdjoefevaczcjfdknpjdyqhttizpngweiqefbdtzgizxwfvaakeglpldjelvdbuhwcgkjnyzlxsz'
    k = 1
    print(s.kDistinctCharacters(t, k))


if __name__ == '__main__':
    main()
