class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 1

    def hash_fun(self, key):
        hf = 0
        for letter in key:
            hf += ord(letter)
        return hf % self.size

    def seek_slot(self, key):
        index = self.hash_fun(key)
        if self.slots[index] is None or self.slots[index] == key:
            return index
        i = (index + self.step) % self.size
        while i != index:
            if self.slots[i] is None or self.slots[i] == key:
                return i
            i = (i + self.step) % self.size
        min(self.hits)
        j = 0
        min_hits = self.hits[0]
        min_hits_index = 0
        while j < self.size:
            if self.hits[j] < min_hits:
                min_hits = self.hits[j]
                min_hits_index = j
            j += 1
        return min_hits_index

    def put(self, key, value):
        index = self.seek_slot(key)
        if self.slots[index] == key and self.values[index] == value:
            return
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def get(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            self.hits[index] += 1
            return self.values[index]
        i = (index + self.step) % self.size
        while i != index:
            if self.slots[i] == key:
                self.hits[i] += 1
                return self.values[i]
            i = (i + self.step) % self.size
        return None

    def __str__(self):
        i = 0
        s = ''
        while i < self.size:
            if self.slots[i] is not None:
                s += f'{i},{self.slots[i]},{self.values[i]}|'
            i += 1
        return s
