from heapq import merge

def sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = sort(left)
    right = sort(right)
    return list(merge(left,right))

import random
test = list(range(20))
random.shuffle(test)
print(test)
print(sort(test))


