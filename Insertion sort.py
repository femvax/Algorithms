def sort(array):
    s_array = array
    for i in range(len(s_array)):
        for j in range(i, 0, -1):
            if s_array[j] < s_array[j - 1]:
                s_array[j], s_array[j - 1] = s_array[j - 1], s_array[j]
    return s_array

import random
test = list(range(10))
random.shuffle(test)
print(test)
print(sort(test))