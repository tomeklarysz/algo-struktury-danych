import time
x = input('type something: ')

x = x.lower()
print(x)

f = open('SJP.txt', 'r')
txt = f.read().splitlines()
# print(len(f.read().splitlines()))

index = int(len(txt)/2)
start = 0
end = len(txt) - 1

stime = time.time()
if len(x.split(' ')) == 1:
    while start <= end:
        if time.time() - stime > 10:
            print('word is not in SJP')
            break
        index = (start + end) // 2
        if x < txt[index]:
            end = index - 1
        elif x > txt[index]:
            start = index + 1
        elif x == txt[index]:
            print('word is in SJP')
            break

print(f'time: {time.time() - stime}')
f.close()