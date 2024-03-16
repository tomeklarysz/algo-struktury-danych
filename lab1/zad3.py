import time

stime = time.time()
piDigits = [3,1,4,1,5,9,2,6,5]

for digit in piDigits:
    print(digit)

print(f'python style time: {time.time() - stime}')
print()

""" cpp style """
stime = time.time()
for i in range(len(piDigits)):
    print(piDigits[i])

print(f'cpp style time: {time.time() - stime}')