if __name__ == '__main__':
    Appetizer = type("Appetizer", (), {})
    shrimp = Appetizer()
    print(type(shrimp))

    Dip = type("Dip", (Appetizer,), {'description': 'Dips are fun things to dip into'})
    salsa = Dip()
    print(type(salsa))
    print(isinstance(salsa, Appetizer))

    Stuffed = type("Stuffed", (Appetizer,), {
        "description": "Things inside things",
        "content_count": 1,
        "total_things": lambda x: x.content_count + 1
    })

    mushrooms = Stuffed()
    print(isinstance(mushrooms, Appetizer))
    print(mushrooms.content_count)
    print(str(mushrooms))


    def to_string(obj):
        return f"OnToast(toppings=f{obj.toppings})"


    OnToast = type("OnToast", (Appetizer,), {
        "toppings": ["tomato", ],
        "__str__": to_string
    })

    bruschetta = OnToast()
    print(str(bruschetta))
