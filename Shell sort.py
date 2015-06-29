def sort(array):
    s_array = array
    d_list = [2 ** i - 1 for i in range((len(s_array) // 2), 0, -1)]  # numbers from Hibbard gap, wiki for details
    for d in d_list:
        for i in range(0, len(s_array) // d):
            for j in range(i*d, 0, -d):
                if s_array[j] < s_array[j - d]:
                    s_array[j], s_array[j - d] = s_array[j - d], s_array[j]
    return s_array

import random
test = list(range(40))
random.shuffle(test)
print(test)
print(sort(test))
