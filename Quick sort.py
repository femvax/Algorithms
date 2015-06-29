
def sort(array):

    if len(array) <= 1:
        return array

    pivot = len(array) // 2
    left = []
    right = []
    med = []
    for el in array:
        if el == array[pivot]:
            med.append(el)
        elif el < array[pivot]:
            left.append(el)
        else:
            right.append(el)

    return sort(left) + med + sort(right)

import random
test = [random.randrange(0,20,1) for x in range(20)]
print(test)
print(sort(test))