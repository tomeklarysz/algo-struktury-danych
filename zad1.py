import statistics
import time

stime = time.time()
myList = [1, 2]
sum = myList[0] + myList[1]
for i in range(2, 48):
    myList.append((myList[i-1] + myList[i-2]) / (myList[i-2] - myList[i-1]))
    sum += myList[i]

avg = sum / len(myList)
# print(avg)

modeList = statistics.multimode(myList)

if len(myList) == len(modeList):
    print('no value appeared more than one time')

print(time.time()-stime)
# 9.584426879882812e-05