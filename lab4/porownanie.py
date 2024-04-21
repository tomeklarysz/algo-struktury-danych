import insertionsort
import mergesort
import random
import time

lista = []
min_insertion = 10.0
min_merge = 10.0
max_insertion = 0.0
max_merge = 0.0
for i in range(100):
    for i in range(1100):
        lista.append(random.randrange(1, 1000))
#     stime = time.time()
#     mergesort.mergesort(lista)
#     etime = time.time()
#     sort_time = float(etime - stime)
#     if (sort_time) < min_merge:
        # min_merge = sort_time
#     if (sort_time) > max_merge:
        # max_merge = sort_time
#     print(f'merge: {sort_time}')
    
    stime = time.time()
    insertionsort.insertionsort(lista)
    etime = time.time()
    sort_time = float(etime - stime)
    if (sort_time) < min_insertion:
        min_insertion = sort_time
    if (sort_time) > max_insertion:
        max_insertion = sort_time
    print(f'insertion: {sort_time}')


# print(min_merge)
# print(max_merge)
print(min_insertion)
print(max_insertion)