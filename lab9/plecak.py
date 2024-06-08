import random
import math
import time

file = open(r'lab9/packages/packages20.txt')
# file = open(r'lab9/packages/packages100.txt')
# file = open(r'lab9/packages/packages500.txt')

dane = []
for l in file:
    x = l.split(',')
    x[-1] = x[-1].replace('\n', '')
    x.pop(0)
    dane.append(x)
dane.pop(0)
dane.pop(0)


def greedy(data, size):
    # zawsze wybieramy przedmiot z najwieksza wartoscia nie patrzac na wymiary
    width = 0
    height = 0
    value = 0
    while height < size and width < size:
        max_value = 0
        max_width = 0
        max_height = 0
        index = 0
        for l in data:
            if int(l[2]) > max_value:
                if width + int(l[0]) <= size and height + int(l[1]) <= size:
                    max_width = int(l[0])
                    max_height = int(l[1])
                    max_value = int(l[2])
                    index = data.index(l)
        width += max_width
        height += max_height
        value += max_value
        data[index][2] = 0
        # print([width, height, value])
        
    return [width, height, value]


def alg_ratio(data, size):
    # wybieramy elementy z najlepszym stosunkiem value / (width + height)
    width = 0
    height = 0
    value = 0
    ratios = []
    for l in data:
            ratio = int(l[2]) / (int(l[0]) + int(l[1]))
            ratios.append(ratio)
    while height < size and width < size:
        max_ratio = 0
        index = 0
        for i in range(len(data)):
            if ratios[i] > max_ratio:
                if width + int(data[i][0]) <= size and height + int(data[i][1]) <= size:
                    max_ratio = ratios[i]
                    index = i
        width += int(data[index][0])
        height += int(data[index][1])
        value += int(data[index][2])
        ratios[index] = 0
        # print([width, height, value])
        
    return [width, height, value]


def simulate(data, size):
    init_temp = 10000.0
    change = 0.95
    final_temp = 0.1
    current_temp = init_temp
    best_width = 0
    best_height = 0
    old_value = 0
    while current_temp > final_temp:
        books = list(data)
        width = 0
        height = 0
        value = 0
        while width <= size and height <= size:
            element = random.choice(books)
            if width + int(element[0]) <= size and height + int(element[1]) <= size:
                width += int(element[0])
                height += int(element[1])
                value += int(element[2])
                books.remove(element)
                # print([width, height, value])
            else:
                break
        value_diff = old_value - value
        p = math.e ** (( - value - old_value) / current_temp)
        if (value_diff < 0
            or random.uniform(0, 1) < p):
            best_width = width
            best_height = height
            old_value = value
        # if i > 0:
            # print(p)
        current_temp *= change
        # print([best_width, best_height, best_value])
    return [best_width, best_height, old_value]


# print(greedy(dane, 20)) # 39
# print(alg_ratio(dane, 20)) # 49
print(simulate(dane, 20))