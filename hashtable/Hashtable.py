class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hf = 0
        for letter in value:
            hf += ord(letter)
        return hf % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        if self.slots[index] is None or self.slots[index] == value:
            return index
        i = index + self.step
        while i != index:
            if self.slots[i] is None or self.slots[i] == value:
                return i
            i = (i + self.step) % self.size
        return None

    def put(self, value):
        slot_index = self.seek_slot(value)
        if slot_index is None:
            return None
        self.slots[slot_index] = value
        return slot_index

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        i = index + self.step
        while i != index:
            if self.slots[i] == value:
                return i
            i = (i + self.step) % self.size
        return None

    def __str__(self):
        i = 0
        s = ''
        while i < self.size:
            s += f'{i}={self.slots[i]},'
            i += 1
        print(s)

