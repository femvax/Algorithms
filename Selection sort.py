def sort(array):
    s_array = array
    for i in range(len(s_array)):
        id_min = i
        for j in range(i+1,len(s_array)):
            if s_array[j] < s_array[id_min]:
                id_min = j
        s_array[i], s_array[id_min] = s_array[id_min], s_array[i]
    return s_array

import random
test = list(range(10))
random.shuffle(test)
print(test)
print(sort(test))