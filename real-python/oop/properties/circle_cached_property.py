from functools import cached_property
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # simulate a complex computation
        return self.radius * 2
