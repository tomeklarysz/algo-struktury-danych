root = [1.5, 3.5, 4.5, 7.5, 9.5]

class Node:
    def __init__(self, root, value):
        self.root = root
        self.value = value
        self.left = None
        self.right = None

nodes = []
for item in root:
    nodes.append(Node(root, item))

nodes[0].left = 1.3
nodes[0].right = 1.6

nodes[1].right = 3.7

nodes[2].left = 4.0
nodes[2].right = 4.99

nodes[3].left = 7.3
nodes[3].right = Node(root, 7.8)
nodes[3].right.left = Node(root, 7.7)
nodes[3].right.right = 7.9
nodes[3].right.left.left = 7.6


def printNodes(node, level):
    print(node.value, end='')
    if node.left:
        print("-"*level, end='')
        if not node.right:
            printNodes(node.left, level+1)
        else:
            print(node.left)
            print(f'{" "*level}{"-"*level}{node.right}')
    elif node.right:
        print("-"*level, end='')
        printNodes(node.right, level+1)
    else:
        print(node.value)

def printTree(tree):
    level = 1
    for node in tree:
        printNodes(node, level)

printTree(nodes)