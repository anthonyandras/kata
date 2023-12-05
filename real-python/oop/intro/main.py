import concurrent.futures


class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def birthday(self):
        self.age += 1


class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def eat(self, food):
        print(f"{self.name} eat {food}")

    def action(self):
        print(f"{self.name} jumps")


class Baby(Person):
    description = "baby"

    def speak(self):
        print("ba ba ba ba ba")

    def nap(self):
        print(f"{self.name} takes a nap")


def do_thing(person: Person, food):
    person.speak()
    person.eat(food)
    person.action()


if __name__ == "__main__":
    # dotty = Dog('Dotty', 13)
    # peanut = Dog('Peanut', 10)
    # print(dotty.description())
    # print(dotty.speak("treats please"))
    # dotty.birthday()
    # print(dotty.description())
    # print(peanut.description())

    person = Person("Anthony", 21)
    baby = Baby("Freddie", 2)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(do_thing, person, 'pasta')
        executor.submit(do_thing, baby, 'apple sauce')
