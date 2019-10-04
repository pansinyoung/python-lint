"""
426. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

(Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)

Example
Example 1:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Explanation: ["255.255.111.35", "255.255.11.135"] will be accepted as well.
Example 2:

Input: "1116512311"
Output: ["11.165.123.11","111.65.123.11"]
Notice
You can return all valid IP address in any order.
"""


class Solution:
    def restoreIpAddresses(self, s):
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s, i, prev, result):
        if i >= len(s) and len(prev) == 4:
            result.append('.'.join(a for a in prev))
            return
        if len(prev) == 4 or i >= len(s):
            return
        if s[i] == '0':
            prev.append('0')
            self.helper(s, i + 1, prev, result)
            prev.pop()
            return
        for j in range(i + 1, i + 4):
            if j <= len(s) and int(s[i:j]) <= 255:
                prev.append(s[i:j])
                self.helper(s, j, prev, result)
                prev.pop()


def main():
    print(Solution().restoreIpAddresses('1116512311'))


if __name__ == '__main__':
    main()