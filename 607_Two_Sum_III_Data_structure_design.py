"""
607. Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""


class TwoSum:
    def __init__(self):
        self.numCount = {}
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        if number in self.numCount:
            self.numCount[number] += 1
        else:
            self.numCount[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for i in self.numCount:
            tar = value - i
            if (tar == i and self.numCount[i] > 1) or (tar != i and tar in self.numCount):
                return True
        return False


def main():
    s = Solution()
    source = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 1
    print(s.searchMatrix(source, target))


if __name__ == "__main__":
    main()
