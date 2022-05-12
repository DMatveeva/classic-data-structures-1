class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.deque.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def __str__(self):
        string = ''
        i = 0
        while i < self.size():
            string += f'{self.deque[i]},'
            i += 1
        return string