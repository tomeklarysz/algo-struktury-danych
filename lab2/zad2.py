f = open('zadanie2.csv', 'r')

myList = []

count = 0
for line in f:
    if count == 0:
        count += 1
        continue
    line = line.replace('\n', '')
    new_line = line.split(',')
    id = int(new_line[0])
    val = new_line[1]
    if val != '':
        myList.append([id, val])
    count += 1

myList.sort()

deletedWords = []
for i in range(len(myList)):
    myList[i][1] = myList[i][1].lower()
    if i+1 < len(myList) and myList[i][0] >= myList[i+1][0]:
        myList[i+1][0] = myList[i][0] + 1
    words = myList[i][1].split(' ')
    for word in words:
        if len(word) >= 2:
            prefix1 = word[0]
            prefix2 = word[1]
            if abs(ord(prefix1) - ord(prefix2)) == 1:
                deletedWords.append([myList[i][0], word])
                words.remove(word)
    myList[i][1] = ''
    myList[i][1] = ' '.join(words)
    # print(myList[i])

for d in deletedWords:
    print(d)

f.close()