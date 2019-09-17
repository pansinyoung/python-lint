"""
74. First Bad Version
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Example
Given n = 5:

    isBadVersion(3) -> false
    isBadVersion(5) -> true
    isBadVersion(4) -> true

Here we are 100% sure that the 4th version is the first bad version.
Challenge
You should call isBadVersion as few as possible.

Notice
Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)
"""
class SVNRepo:
   @classmethod
   def isBadVersion(cls, id):
       return [True][id - 1]
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n: int) -> int:
        # if n == 1:
        #     return 1
        start, end = 1, n
        while start < end - 1:
            mid = (start + end) // 2
            cur = SVNRepo.isBadVersion(mid)
            if cur and (mid == 1 or not SVNRepo.isBadVersion(mid - 1)):
                return mid
            if cur:
                end = mid
            else:
                start = mid
        return start if SVNRepo.isBadVersion(start) else end



def main():
    s = Solution()

    print(s.findFirstBadVersion(1))


if __name__ == '__main__':
    main()
