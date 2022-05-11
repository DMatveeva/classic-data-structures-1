from stack.Stack import Stack


class QueueWithStacks:
    def __init__(self):
        self.stack_for_enqueue = Stack()
        self.stack_for_dequeue = Stack()

    def enqueue(self, item):
        i = 0
        while self.stack_for_dequeue.peek() is not None:
            self.stack_for_enqueue.push(self.stack_for_dequeue.pop())
            i += 1
        self.stack_for_enqueue.push(item)

    def dequeue(self):
        if self.stack_for_dequeue.size() == 0 and self.stack_for_enqueue.size() == 0:
            return None
        else:
            i = 0
            while self.stack_for_enqueue.peek() is not None:
                self.stack_for_dequeue.push(self.stack_for_enqueue.pop())
                i += 1
            return self.stack_for_dequeue.pop()

    def size(self):
        return self.stack_for_dequeue.size() or self.stack_for_enqueue.size()

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        i = 0
        while i < self.size():
            if self.queue[i] != other.queue[i]:
                return False
            i += 1
        return True

    def __str__(self):
        string = ''
        i = 0
        string += 'enqueue: ' + self.stack_for_enqueue.__str__()
        string += '   dequeue: ' + self.stack_for_dequeue.__str__()
        return string