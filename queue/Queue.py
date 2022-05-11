class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

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
        while i < self.size():
            string += f'{self.queue[i]},'
            i += 1
        return string