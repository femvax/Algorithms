import random

def sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)

    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    med = [x for x in array if x == pivot]

    return sort(left) + med + sort(right)

test = [random.randrange(0,20,1) for x in range(20)]
print(test)
print(sort(test))