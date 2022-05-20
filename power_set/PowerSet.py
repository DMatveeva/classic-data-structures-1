class PowerSet:

    def __init__(self):
        self.values = {}

    def size(self):
        return len(self.values)

    def put(self, value):
        self.values[value] = value

    def get(self, value):
        return True if self.values.get(value) is not None else False

    def remove(self, value):
        return True if self.values.pop(value, None) is not None else False

    def intersection(self, set2):
        new_set = PowerSet()
        for key in self.values.keys():
            if set2.get(key):
                new_set.put(key)
        return new_set

    def union(self, set2):
        new_set = PowerSet()
        for key in self.values.keys():
            new_set.put(key)
        for key2 in set2.values.keys():
            if not self.get(key2):
                new_set.put(key2)
        return new_set

    def difference(self, set2):
        new_set = PowerSet()
        for key2 in set2.values.keys():
            if not self.get(key2):
                new_set.put(key2)
        return new_set

    def issubset(self, set2):
        for key2 in set2.values.keys():
            if not self.get(key2):
                return False
        return True

    def __str__(self):
        i = 0
        s = ''
        for key in self.values.keys():
            s = s + f'{str(key)},'
        return s
