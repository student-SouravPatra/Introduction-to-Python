# Assignment 8 - Program 2
# Equilateral Triangle using Inheritance

import math


class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class Equilateral(Triangle):
    def calculate_area(self):
        return (math.sqrt(3) / 4) * self.side1 ** 2

    def find_tangents(self):
        print("Tan of Angle 1:", math.tan(math.radians(self.angle1)))
        print("Tan of Angle 2:", math.tan(math.radians(self.angle2)))
        print("Tan of Angle 3:", math.tan(math.radians(self.angle3)))


# Create Equilateral Triangle object
triangle = Equilateral(6, 6, 6, 60, 60, 60)

print("Side 1:", triangle.side1)
print("Side 2:", triangle.side2)
print("Side 3:", triangle.side3)

print("Angle 1:", triangle.angle1)
print("Angle 2:", triangle.angle2)
print("Angle 3:", triangle.angle3)

print("Area of Equilateral Triangle:", triangle.calculate_area())

print("\nTangent of all angles:")
triangle.find_tangents()
