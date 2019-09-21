"""
600. Smallest Rectangle Enclosing Black Pixels
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example
Example 1:

Input：["0010","0110","0100"]，x=0，y=2
Output：6
Explanation：
The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
Example 2:

Input：["1110","1100","0000","0000"], x = 0, y = 1
Output：6
Explanation：
The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).
"""
from typing import List


class Solution:
    def check_row(self, image: List[str], i: int) -> bool:
        for c in image[i]:
            if c == '1':
                return True
        return False

    def check_col(self, image: List[str], i: int) -> bool:
        for line in image:
            if line[i] == '1':
                return True
        return False

    def minArea(self, image: List[str], x: int, y: int) -> int:
        if not image:
            return 0
        m, n = len(image), len(image[0])
        if not n:
            return 0

        start, end = 0, x
        while start < end - 1:
            mid = (start + end) // 2
            if not self.check_row(image, mid):
                start = mid + 1
            else:
                end = mid
        x1 = start if self.check_row(image, start) else end
        start, end = x, m - 1
        while start < end - 1:
            mid = (start + end) // 2
            if not self.check_row(image, mid):
                end = mid - 1
            else:
                start = mid
        x2 = end if self.check_row(image, end) else start

        start, end = 0, y
        while start < end - 1:
            mid = (start + end) // 2
            if not self.check_col(image, mid):
                start = mid + 1
            else:
                end = mid
        y1 = start if self.check_col(image, start) else end
        start, end = y, n - 1
        while start < end - 1:
            mid = (start + end) // 2
            if not self.check_col(image, mid):
                end = mid - 1
            else:
                start = mid
        y2 = end if self.check_col(image, end) else start
        return (x2 - x1 + 1) * (y2 - y1 + 1)


def main():
    s = Solution()
    # source = ["000000000000",
    #           "000000000000",
    #           "000000000000",
    #           "000000000000",
    #           "000000000000",
    #           "000000000000",
    #           "000000000001",
    #           "000000000001",
    #           "000000000001"]
    # x = 6
    # y = 11
    source = ["1110","1100","0000","0000"]
    x = 0
    y = 1
    print(s.minArea(source, x, y))


if __name__ == '__main__':
    main()
