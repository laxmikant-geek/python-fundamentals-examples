"""A small shape hierarchy demonstrating inheritance, super(), and overriding.

Run it: python shapes.py
Part of the Python Fundamentals series on GeeksArray.
"""

import math
from dataclasses import dataclass


class Shape:
    """Base class: every shape has a name and can report its area."""

    def __init__(self, name):
        self.name = name

    def area(self):
        # Subclasses must override this.
        raise NotImplementedError("Subclasses must implement area()")

    def __str__(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")   # reuse the parent's setup
        self.radius = radius

    def area(self):  # override
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):  # override
        return self.width * self.height


@dataclass
class Point:
    """A dataclass: __init__, __repr__, and __eq__ generated for us."""
    x: float
    y: float


if __name__ == "__main__":
    shapes = [Circle(2), Rectangle(3, 4)]
    for s in shapes:
        # Polymorphism: the same call does the right thing per object.
        print(s)

    p1 = Point(1.0, 2.0)
    p2 = Point(1.0, 2.0)
    print(p1)              # Point(x=1.0, y=2.0)
    print("Equal?", p1 == p2)   # True, thanks to dataclass
