#MyModule

import math

class circle:
    def __init__(self, radius):
        self.radius = radius
    def pole(self):
        return math.pi * math.pow(self.radius, 2)
    def obwod(self):
        return 2 * math.pi * self.radius

class square:
    def __init__(self, a):
        if a <= 0:
            print('square can\'t have negative side length')
        else:
            self.a = a
    def pole(self):
        return math.pow(self, 2)
    def obwod(self):
        return 4 * self.a
    
class triangle:
    def __init__(self, a, b, c):
        if (a+b<c) or (a+c<b) or (b+c<a):
            print('these values can\'t create a triangle')
        else:
            self.a = a
            self.b = b
            self.c = c