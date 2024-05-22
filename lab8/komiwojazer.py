import math
from numpy import random
import numpy as np

cords = []
f = open('lab8/TSP.txt')
for l in f:
    x = l.split()
    x.pop(0)
    cords.append(x)

# print(cords)

path = np.array(range(100))
random.shuffle(path)


def path_length(path):
    length = 0
    for i in range(len(path)):
        first_index = path[i]
        if i == len(path) - 1:
            second_index = path[0]
        else:
            second_index = path[i+1]
        cur = pow(float(cords[first_index-1][0]) - float(cords[second_index-1][0]), 2)
        cur += pow(float(cords[first_index-1][1]) - float(cords[second_index-1][1]), 2)
        length += math.sqrt(cur)
    return length

# print(path_length([1, 2]))
# print(path_length(path))

# w kolejnosci takiej jak w pliku
x = path_length(range(100))
print(x)

# greedy
def greedy(cords):
    
    start = cords.pop(0)
    end = 0
    length = 0
    current_index = 0
    while len(cords) > 0:
        min = 0
        index = 0
        for i in range(len(cords)):
            cur = pow(float(cords[current_index][0]) - float(cords[i][0]), 2)
            cur += pow(float(cords[current_index][1]) - float(cords[i][1]), 2)
            cur = math.sqrt(cur)
            if min == 0:
                min = cur
                index = i
            else:
                if cur < min:
                    min = cur
                    index = i
        if len(cords) == 0:
            end = cords[current_index]
        cords.pop(current_index)
        current_index = index
        length += min
    # adding start
            