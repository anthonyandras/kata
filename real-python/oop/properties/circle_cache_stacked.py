from functools import cache
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    @cache
    def diameter(self):
        """immutable diameter - nuanced use case"""
        sleep(0.5)  # simulate a complex computation
        return self.radius * 2
