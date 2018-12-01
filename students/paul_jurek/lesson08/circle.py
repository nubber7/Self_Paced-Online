"""Circle generation Class
This is part of Lesson 8 for UW Python 201 course
This generates a circle and related methods to
practice OOP and TDD
reference: https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2018_Winter/courseware/0e928204424a407eac492ebcd2f69adb/d57639f9f0a8498f8578550886710867/?child=first"""

import math

class Circle:
    """circle geometry object"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value/2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        """when another circle is added, create new circle
        with added radius
        when number is added, modify existing circle"""
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            self.radius += other

    def __mul__(self, other):
        self.radius *= other

    def __rmul__(self, other):
        self.radius *= other