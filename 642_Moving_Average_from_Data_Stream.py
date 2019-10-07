"""
642. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
"""
import collections


class MovingAverage:
    def __init__(self, size):
        self.data = collections.deque()
        self.sum = 0
        self.max_size = size

    def next(self, val):
        if self.max_size == 0:
            return 0
        if len(self.data) < self.max_size:
            self.sum += val
            self.data.append(val)
            return self.sum / len(self.data)
        self.sum += val - self.data.popleft()
        self.data.append(val)
        return self.sum / len(self.data)


if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(2))
    print(m.next(3))
    print(m.next(4))
    print(m.next(5))
    print(m.next(6))
    print(m.next(7))
