from collections import deque
stack = deque()

class StackQueue:

    def __init__(self):
        self.container = deque()
        self.buffer = deque()

    def stack_push(self, val):
        self.container.append(val)
        return

    def stack_peek(self):
        return self.container[-1]

    def queue_enqueue(self, val):
        self.buffer.appendleft(val)

    def queue_dequeue(self):
        return self.buffer.pop()
    

        

s = StackQueue()
s.stack_push("https://theconscienceproject.com")
print(s.stack_peek())
q = StackQueue()
q.queue_enqueue('Probal')
print(q.queue_dequeue())


