class Point:
    """Example of using getter/setter Java-like methods in Python, don't do this"""

    # def __init__(self, x, y):
    #     self._x = x
    #     self._y = y
    #
    # def get_x(self):
    #     return self._x
    #
    # def set_x(self, value):
    #     self._x = value
    #
    # def get_y(self):
    #     return self._y
    #
    # def set_y(self, value):
    #     self._y = value
    def __init__(self, x, y):
        """This is more pythonic"""
        self.x = x
        self.y = y
