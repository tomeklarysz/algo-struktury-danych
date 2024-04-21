import random

def mergesort(A):
    length = len(A)

    if length == 1:
        return A
    
    middle = length // 2
    left_half = A[:middle]
    right_half = A[middle:]
    left = mergesort(left_half)
    right = mergesort(right_half)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(list(left[i:]))
    result.extend(list(right[j:]))
    return result

lista = []
for i in range(100):
    lista.append(random.randrange(1, 1000))

# print(lista)
# print(mergesort(lista))