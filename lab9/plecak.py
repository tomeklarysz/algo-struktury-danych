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


print(greedy(dane, 20)) # 39
# print(alg_ratio(dane, 20)) # 49