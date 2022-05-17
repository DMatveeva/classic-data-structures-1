class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hf = 0
        for letter in key:
            hf += ord(letter)
        return hf % self.size

    def is_key(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return True
        i = (index + 1) % self.size
        while i != index:
            if self.slots[i] == key:
                return True
            i = (i + 1) % self.size
        return False

    def seek_slot(self, key):
        index = self.hash_fun(key)
        if self.slots[index] is None or self.slots[index] == key:
            return index
        i = (index + 1) % self.size
        while i != index:
            if self.slots[i] is None or self.slots[i] == key:
                return i
            i = (i + 1) % self.size

    def put(self, key, value):
        index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return self.values[index]
        i = (index + 1) % self.size
        while i != index:
            if self.slots[i] == key:
                return self.values[i]
            i = (i + 1) % self.size
        return None

    def __str__(self):
        i = 0
        s = ''
        while i < self.size:
            if self.slots[i] is not None:
                s += f'{i},{self.slots[i]},{self.values[i]}|'
            i += 1
        return s
