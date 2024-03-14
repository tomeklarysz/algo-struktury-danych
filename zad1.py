import statistics

myList = [1, 2]
sum = myList[0] + myList[1]
for i in range(2, 48):
    myList.append((myList[i-1] + myList[i-2]) / (myList[i-2] - myList[i-1]))
    sum += myList[i]

avg = sum / len(myList)
# print(avg)

mode = statistics.multimode(myList)
for num in mode:
    print(num)