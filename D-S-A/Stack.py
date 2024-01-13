from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack = Stack()
    # stack.push(4)
    stack.push(3)
    stack.push(2)
    print(stack.is_empty())
    stack.push(1)
    print(stack.size())
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    # stack.pop()  # OUT OF RANGE
    print(stack.is_empty())
    stack.push([4, 5])
    print(stack.peek())
