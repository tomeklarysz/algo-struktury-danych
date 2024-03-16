myList = [10,20,30]

denominator = 0

try:
    nominator = myList[3]
    result = nominator / denominator
    print(result)
except IndexError:
    print('Wrong index')
    nominator = myList[2]

try:
    nominator = myList[2]
    result = nominator / denominator
    print(result)
except ZeroDivisionError:
    print("Can't divide by 0")
    denominator = 10

try:
    nominator = myList[2]
    result = nominator / denomintor
    print(result)
except NameError:
    print("Wrong name")
    denominator = 10
    result = nominator / denominator
except:
    print("Unknown error")
    result = 10