class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[self.size() - 1]

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        i = 0
        while i < self.size():
            if self.stack[i] != other.stack[i]:
                return False
            i += 1
        return True

    def __str__(self):
        string = ''
        i = 0
        while i < self.size():
            string += f'{self.stack[i]},'
            i += 1
        return string
