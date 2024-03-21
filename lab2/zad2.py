f = open('zadanie2.csv', 'r')

myList = []
txt = f.read()
lines = txt.splitlines()


print(f'starting length: {len(lines)}')
for line in lines:
    new_line = line.split(',')
    val = new_line[1]
    # print(new_line)
    if val != '':
        myList.append(new_line)

        
# print(myList[-2])
print(f'new length: {len(myList)}')

for i in range(1, len(myList)):
    myList[i][0] = int(myList[i][0])


myList.sort()
print(myList)

f.close()
