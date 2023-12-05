def new(cls):
    obj = object.__new__(cls)
    obj.description = "Amuse your brain"
    return obj


class CounterMeta(type):
    count = 0

    def __new__(cls, name, bases, dct):
        kls = super().__new__(cls, name, bases, dct)
        cls.count += 1
        return kls


class Pie(metaclass=CounterMeta):
    pass


class Cake(metaclass=CounterMeta):
    pass


if __name__ == '__main__':
    AmuseBouche = type("AmuseBouche", (), {
        "__new__": new,
    })
    ceviche = AmuseBouche()
    print(ceviche.description)

    apple = Pie()
    raspberry = Pie()
    print(apple.__class__.count)

    chocolate = Cake()
    vanilla = Cake()
    print(vanilla.__class__.count)
