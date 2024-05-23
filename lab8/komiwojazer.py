import math
from numpy import random
import numpy as np

cords = []
f = open('lab8/TSP.txt')
for l in f:
    x = l.split()
    x.pop(0)
    cords.append(x)

# path = np.array(range(100))
# random.shuffle(path)


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


# z = path_length(path)
# print(f'random path length: {z}')

# w kolejnosci takiej jak w pliku
x = path_length(range(100))
print(f'dlugosc po kolei: {x}')

# greedy
def greedy(cords):
    
    visited = []
    start = cords[0]
    length = 0
    current_index = 0
    while len(visited) < len(cords) - 1:
        min = 0
        index = 0
        for i in range(len(cords)):
            if (i not in visited) and i != current_index:
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
        visited.append(current_index)
        current_index = index
        length += min
    cur = pow(float(cords[current_index][0]) - float(start[0]), 2)
    cur += pow(float(cords[current_index][1]) - float(start[1]), 2)
    length += math.sqrt(cur)
    return length

y = greedy(cords)
print(f'metoda zachlanna: {y}')