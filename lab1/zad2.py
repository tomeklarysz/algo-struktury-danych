from array import *
import statistics
import time

stime = time.time()

myArray = array('f', [1, 2])
sum = myArray[0] + myArray[1]
for i in range(2, 48):
    myArray.append((myArray[i-1] + myArray[i-2]) / (myArray[i-2] - myArray[i-1]))
    sum += myArray[i]

avg = sum / len(myArray)
# print(avg)

modeList = statistics.multimode(myArray)

if len(myArray) == len(modeList):
    print('no value appeared more than one time')

print(time.time()-stime)