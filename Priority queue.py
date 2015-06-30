class PriorityQueue:

    def __init__(self):
        self.values = []
        self.keys = []

    def insert(self, value, key):
        self.values.append(value)
        self.keys.append(key)

    def extract(self):
        i = self.keys.index(max(self.keys))
        del self.keys[i]
        return self.values.pop(i)