import random
import math

def randomPoint(x1, x2, y1, y2):
    return random.uniform(x1, x2), random.uniform(y1, y2)

def monteCarloSinus(x1, x2, y1, y2):
    areaRectangle = abs(x1-x2)*abs(y1-y2)
    allPoints = 100000
    validPointsCounter = 0
    for i in range(allPoints):
        point = randomPoint(x1, x2, y1, y2)
        if math.sin(point[0]) > point[1]:
            validPointsCounter += 1
    # print(validPointsCounter)
    return (areaRectangle * validPointsCounter) / allPoints

print(monteCarloSinus(0, 2, 0, 1))