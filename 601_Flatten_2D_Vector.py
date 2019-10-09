"""
601. Flatten 2D Vector
Implement an iterator to flatten a 2d vector.

Example
Example 1:

Input:[[1,2],[3],[4,5,6]]
Output:[1,2,3,4,5,6]
Example 2:

Input:[[7,9],[5]]
Output:[7,9,5]
"""


class Vector2D(object):

    def __init__(self, vec2d):
        self.data = vec2d
        self.row, self.col = 0, 0
        self.nextElem = None
        self.findNext()

    def findNext(self):
        self.nextElem = None
        while self.row < len(self.data):
            if not self.data[self.row] or self.col + 1 >= len(self.data[self.row]):
                self.row += 1
                self.col = 0
            else:
                self.nextElem = self.data[self.row][self.col]
                break

    def next(self):
        result = self.nextElem
        self.findNext()
        return result

    def hasNext(self):
        return bool(self.nextElem)


if __name__ == '__main__':
    v = Vector2D([[1, 2], [3], [4, 5, 6]])
    print(v.next())