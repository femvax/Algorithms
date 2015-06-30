class BinaryHeap:

    def __init__(self):
        self.heap = []

    def insert(self, key, value):
        self.heap.append((key, value))
        self.check_up(len(self.heap) - 1)

    def check_up(self, i):
        if i > 0:
           if self.heap[i][0] < self.heap[i // 2][0]:
               self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
           self.check_up(i // 2)

    def check_down(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left][0] < self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[largest][0]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self. heap[largest]
            self.check_down(largest)

    def extract(self):
        ext = self.heap[0][1]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
        self.check_down(0)
        return ext

def sort(array,key):
    s_array = BinaryHeap()
    for i in array:
        s_array.insert(i,key(i))
    return [s_array.extract() for i in array]

