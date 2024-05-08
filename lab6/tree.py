root = [1.5, 3.5, 4.5, 7.5, 9.5]

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
            self.array.append(x)
            return
        for i in range(len(self.array)):
            if x > self.array[i].value and x < self.array[i+1].value:
                if x - self.array[i].value > 0.5:
                    self.array[i+1].insert(x)
                    return
                self.array[i].insert(x)
                return
                           

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


arr = TreeArray(10)
arr.insert(0.6)
arr.insert(3.2)
arr.insert(2.7)
arr.insert(2.8)
arr.insert(1.2)
arr.insert(2.6)
arr.insert(3.7)
arr.insert(3.3)
arr.insert(3.1)

arr.printTreeArray()