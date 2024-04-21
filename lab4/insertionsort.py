import random

def insertionsort(A):
    if len(A) == 1:
        return A
    for i in range(1, len(A)):
        value = A[i]
        j = i -1
        while j >= 0 and A[j] > value:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = value
    return A

lista = []
for i in range(100):
        lista.append(random.randrange(1, 100))

# print(insertionsort(lista))