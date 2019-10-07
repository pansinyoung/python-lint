"""
494. Implement Stack by Two Queues
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Example
Example 1:

Input:
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
Example 2:

Input:
isEmpty()
"""
import collections


class Stack:
    queue1 = collections.deque()
    queue2 = collections.deque()
    length = 0

    def push(self, x):
        self.queue1.append(x)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        cur = None
        while self.queue1:
            cur = self.queue1.popleft()
            if not self.queue1:
                break
            self.queue2.append(cur)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return cur

    def top(self):
        if not self.queue1:
            return None
        cur = None
        while self.queue1:
            cur = self.queue1.popleft()
            self.queue2.append(cur)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return cur

    def isEmpty(self):
        return self.length == 0
