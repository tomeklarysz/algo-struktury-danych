import time

stime = time.time()
piDigits = [3,1,4,1,5,9,2,6,5]

for digit in piDigits:
    print(digit)

print(f'python style time: {time.time() - stime}')
# 3.2901763916015625e-05
print()

""" cpp style """
stime = time.time()
for i in range(len(piDigits)):
    print(piDigits[i])

print(f'cpp style time: {time.time() - stime}')
# 1.9550323486328125e-05