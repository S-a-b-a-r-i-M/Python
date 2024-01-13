from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enque(self, val):
        self.queue.append(val)

    def deque(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError('Queue is empty')

    def extend(self, sequence_val):
        for val in sequence_val:
            self.enque(val)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError('Queue is empty')

    def is_empty(self) -> bool:
        return len(self.queue) <= 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


my_queue = Queue()
my_queue.enque(1)
my_queue.enque(2)
my_queue.extend([3, 4, 5])

print(my_queue)

print(my_queue.deque(),my_queue.deque(),my_queue.deque(),my_queue.deque(),
      my_queue.deque())

print(my_queue.deque()) # ACCESSING EMPTY QUEUE
