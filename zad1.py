list = [1, 2]
avg = list[0] + list[1]
mode = 0
for i in range(2, 47):
    list.append((list[i-1] + list[i-2]) / (list[i-2] - list[i-1]))
    avg += list[i]

avg /= 48
print(avg)