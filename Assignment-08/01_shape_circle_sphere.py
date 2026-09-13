# Assignment 8 - Program 1
# Shape, Circle and Sphere using Inheritance

import math


class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def calculate_area(self):
        return math.pi * self.radius ** 2


class Sphere(Shape):
    def calculate_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


# Create Circle object
circle = Circle(5)

print("Circle Radius:", circle.radius)
print("Area of Circle:", circle.calculate_area())


# Create Sphere object
sphere = Sphere(5)

print("\nSphere Radius:", sphere.radius)
print("Volume of Sphere:", sphere.calculate_volume())
