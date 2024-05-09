import math
import time
import random
class TreeArray:
    def __init__(self, length):
        self.length = length
        array = []
        for i in range(1, length, 1):
            array.append(Node(i-0.5))
        self.array = array
    
    def printTreeArray(self):
        for node in self.array:
            # if node.left is not None or node.right is not None:
                # node.printTree()
            node.printTree()
    
    def insert(self, x):
        if x < self.array[0].value:
            self.array[0].insert(x)
            return
        if x > self.array[-1].value:
            self.array[-1].insert(x)
            return
        for i in range(len(self.array)):
            if x > self.array[i].value and x < self.array[i+1].value:
                if x - self.array[i].value > 0.5:
                    self.array[i+1].insert(x)
                    return
                self.array[i].insert(x)
                return

    def minimum(self, y):
        return self.array[y].minimum()
    
    def maximum(self, y):
        return self.array[y].maximum()
    
    def search(self, x):
        return self.array[math.floor(x)].search(x)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def printTree(self, level=0, isRight=False):
        if isRight:
            print('    ', ' ' * 5 * (level-1), end='')
        print('-'*level, self.value, end='')
        print(' ', end='')
        if self.left:
            self.left.printTree(level+1)
        if self.right:
            self.right.printTree(level+1, isRight=self.left is not None)
        if (not self.left) and (not self.right):
            print()
    
    def insert(self, x):
        if not self.value:
            self.value = x
            return
        if self.value == x:
            return
        if x < self.value:
            if self.left:
                self.left.insert(x)
                return
            self.left = Node(x)
            return
        if self.right:
            self.right.insert(x)
            return
        self.right = Node(x)
    
    def minimum(self):
        temp = self
        while temp.left:
            temp = temp.left
        return temp.value
    
    def maximum(self):
        temp = self
        while temp.right:
            temp = temp.right
        return temp.value
    
    def search(self, x):
        if self.value == x:
            return True
        if x < self.value:
            if self.left:
                return self.left.search(x)
            return False
        if self.right:
            return self.right.search(x)
        return False

arr = TreeArray(11)
# arr.printTreeArray()
sum = 0
number = 100000
for i in range(number):
    stime = time.time()
    arr.insert(random.uniform(0, 10))
    sum += time.time() - stime
print(sum / number)
# print(time.time())
# arr.maximum(3)
# print(time.time())
# arr.minimum(3)
# print(time.time())
# print('search:')
# arr.search(random.uniform(0, 10))
# print(time.time())
