import math


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """Only has access to the class itself, not the "self" object"""
        return f"class method called {cls}"

    @staticmethod
    def staticmethod():
        """No arguments to the class or object instance at all, pretty much a namespaced function"""
        return 'static method called'


class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients,
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def marghertia(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi
