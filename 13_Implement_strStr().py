"""
Description
For a given source string and a target string, you should output the first index(from 0) of target string in source
string.

If target does not exist in source, just return -1.

Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic
implementation ability. But make sure you confirm with the interviewer first.


Example
Example 1:
Input: source = "source" ，target = "target"
Output: -1
Explanation: If the source does not contain the target content, return - 1.

Example 2:
Input:source = "abcdabcdefg" ，target = "bcd"
Output: 1
Explanation: If the source contains the target content, return the location where the target first appeared in the
source.


Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""
from typing import List


class Solution:

    def KMPParttern(self, target: str) -> List[int]:
        if len(target) == 0:
            return []
        if len(target) == 1:
            return [0]
        result = [0] * len(target)
        i = 1
        while i < len(target):
            if target[i] == target[result[i-1]]:
                result[i] = result[i-1] + 1
            i += 1
        return result

    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source: str, target: str) -> int:
        if source == target or target == '':
            return 0
        if len(source) < len(target):
            return -1
        lps = self.KMPParttern(target)
        j = 0
        # print(lps)
        for i in range(len(source)):
            # print(i, j)
            if len(source) - i < len(target) - j:
                break
            if source[i] == target[j]:
                if j == len(target) - 1:
                    return i - len(target) + 1;
                j += 1
            else:
                while True:
                    if j == 0:
                        break
                    j = lps[j - 1]
                    if source[i] == target[j]:
                        j += 1
                        break
        return -1


def main():
    s = Solution()
    source1 = 'mississippi'
    target1 = 'issip'
    source2 = 'source'
    target2 = 'se'
    source3 = 'tartarget'
    target3 = 'target'
    print(source1, target1, s.strStr(source1, target1))
    print(source2, target2, s.strStr(source2, target2))
    print(source3, target3, s.strStr(source3, target3))
    # print('abcdabcdefg', 'bcd', s.strStr('abcdabcdefg', 'bcd'))
    # print(s.KMPParttern('aaaabaacd'))


if __name__ == '__main__':
    main()
