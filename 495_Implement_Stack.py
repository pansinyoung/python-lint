"""
495. Implement Stack
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

Example
Example 1:

Input:
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
Example 2:

Input:
isEmpty()

"""


class Stack:
    stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack
