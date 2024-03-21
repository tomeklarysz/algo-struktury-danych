myList = []
for i in range(500, 3001):
    if i%7 == 0 and i%5 != 0:
        myList.append(i)

string = ''.join(str(item) for item in myList)
print(string)
print(string.count('21'))
print(string.replace('21', 'XX'))