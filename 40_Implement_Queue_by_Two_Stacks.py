"""
40. Implement Queue by Two Stacks
中文English
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
Example 1:

Input:
    push(1)
    pop()
    push(2)
    push(3)
    top()
    pop()
Output:
    1
    2
    2
Example 2:

Input:
    push(1)
    push(2)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(1)
Output:
[]
Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

Notice
Suppose the queue is not empty when the pop() function is called.
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def pop(self):
        if not self.stack1:
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        result = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return result

    def top(self):
        return self.stack1[0] if self.stack1 else None
