"""
class Point:
    def reset(self):
        self.x = 0
        self.y = 0


a = Point()

a.x = 10
a.y = 10

print(a.x, a.y)

a.reset()
print(a.x, a.y)
"""

import math


class Point:
    def __init__(self, xPosition, yPosition):
        self.x = xPosition
        self.y = yPosition

    def move(self, xPosition, yPosition):
        self.x = xPosition
        self.y = yPosition

    def reset(self):
        self.x = 0
        self.y = 0

    def distanceCalc(self, otherPoint):
        return math.sqrt((self.x - otherPoint.x) ** 2 +
                         (self.y - otherPoint.y) ** 2)


point1 = Point(0, 0)
point2 = Point(100, 9999)
print(f"Point1 : ({point1.x}, {point1.y})")
print(f"Point2 : ({point2.x}, {point2.y})")
print(f"Distance : {point1.distanceCalc(point2)}")
