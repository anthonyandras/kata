from random import choice


class Pet:
    def __new__(cls, *args, **kwargs):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I'm a {type(instance).__name__}")
        return instance

    def __init__(self):
        print("Never Runs!")


class Dog:
    def communicate(self):
        print("woof woof")


class Cat:
    def communicate(self):
        print("meow meow")


class Python:
    def communicate(self):
        print("hiss hiss")


if __name__ == '__main__':
    pet = Pet()
    pet.communicate()
    isinstance(pet, Pet)
    isinstance(pet, Dog)
    isinstance(pet, Cat)
    isinstance(pet, Python)
