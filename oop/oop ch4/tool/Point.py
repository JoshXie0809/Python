import math


class Point:
    """Represents a point in two-dimensional geometric coordinates"""

    def __init__(self, xPosition: float, yPosition: float):
        """
        Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.
        """
        self.x = xPosition
        self.y = yPosition

    def move(self, xPosition: float, yPosition: float):
        """Move the point to a new location in 2D space."""
        self.x = xPosition
        self.y = yPosition

    def reset(self):
        """Reset the point back to the geometric origin: 0, 0"""
        self.move(0, 0)

    def distanceCalc(self, otherPoint):
        """
        Calculate the distance from this point to a second 
        point passed as a parameter. This function uses the 
        Pythagorean Theorem to calculate the distance between 
        the two points. The distance is returned as a float.
        """

        return math.sqrt((self.x - otherPoint.x) ** 2 +
                         (self.y - otherPoint.y) ** 2)
