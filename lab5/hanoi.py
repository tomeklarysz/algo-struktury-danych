counter = 0
def Hanoi(n, source, destination, buff):
    global counter
    if n == 0:
        return
    Hanoi(n-1, source, buff, destination)
    destination.append(source.pop())
    counter += 1
    Hanoi(n-1, buff, destination, source)


def iterative(n, source, destination, buff):
    global counter
    counter = 0
    while len(source) != 0 or len(buff) != 0:
        counter += 1
        if counter%3 == 1:
            if len(destination) == 0:
                destination.append(source.pop())
            elif len(source) == 0:
                source.append(destination.pop())
            elif destination[-1] > source[-1]:
                destination.append(source.pop())
            else:
                source.append(destination.pop())
        if counter%3 == 2:
            if len(buff) == 0:
                buff.append(source.pop())
            elif len(source) == 0:
                source.append(buff.pop())
            elif buff[-1] > source[-1]:
                buff.append(source.pop())
            else:
                source.append(buff.pop())
        if counter%3 == 0:
            if len(destination) == 0:
                destination.append(buff.pop())
            elif len(buff) == 0:
                buff.append(destination.pop())
            elif destination[-1] > buff[-1]:
                destination.append(buff.pop())
            else:
                buff.append(destination.pop())
        print(f'source: {source}, buff: {buff}, destination: {destination}')
    return

# a = [6, 5, 4, 3, 2, 1]
a = [4, 3, 2, 1]
b = []
c = []

print(f'START: source: {a}, buff: {b}, destination: {c}')
Hanoi(4, a, b, c)
# iterative(5, a, b, c)
print(counter)
print(f'END: source: {a}, buff: {b}, destination: {c}')