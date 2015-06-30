class BinaryHeap:

    def __init__(self):
        self.heap = []

    def insert(self, key, value):
        self.heap.append((key,value))
        self.heapify(len(self.heap) - 1)

    def heapify(self, i):
        if i > 0:
           if self.heap[i][0] < self.heap[i // 2][0]:
               self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
           self.heapify(i // 2)

    def extract(self):
        ext = self.heap.pop(0)[1]
        self.heapify(len(self.heap) - 1)
        return ext