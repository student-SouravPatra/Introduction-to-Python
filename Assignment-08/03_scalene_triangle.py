# Assignment 8 - Program 3
# Scalene Triangle using Inheritance

import math


class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class Scalene(Triangle):
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        perimeter = self.calculate_perimeter()
        s = perimeter / 2

        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        return area


# Create Scalene Triangle object
triangle = Scalene(5, 6, 7, 60, 50, 70)

print("Side 1:", triangle.side1)
print("Side 2:", triangle.side2)
print("Side 3:", triangle.side3)

print("Perimeter:", triangle.calculate_perimeter())

area = triangle.calculate_area()

print("Area:", area)
print("Area as Whole Number:", round(area))
