from datetime import date
from functools import singledispatchmethod
# third party libraries for handling dispatch with multiple arguments
# this really should just be included in the stdlib
# multipledispatch
# multimethod -- definitely seems to be preferred


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise ValueError(f"unsupported date format: {birth_date}")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.date = birth_date

    @__init__.register(str)
    def _from_isoformat(self, birth_date):
        self.date = date.fromisoformat(birth_date)

    @__init__.register(int)
    @__init__.register(float)
    def _from_timestamp(self, birth_date):
        self.date = date.fromtimestamp(birth_date)

    def age(self):
        return date.today().year - self.date.year


class Person:
    def __init__(self, name, birth_date):
        """Works, but doesn't scale well, considered an anti-pattern - see PEP-0443"""
        self.name = name
        self._birth_info = BirthInfo(birth_date)

    @property
    def age(self):
        return self._birth_info.age()

    @property
    def birth_date(self):
        return self._birth_info.date


if __name__ == '__main__':
    jane = Person("Jane Done", "2000-11-29")
    print(jane.birth_date)

    john = Person("John Doe", date(1998, 5, 15))
    print(john.birth_date)

    linda = Person("Linda Smith", 1011222000)
    print(linda.birth_date)
