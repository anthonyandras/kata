class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value


class B:
    def __new__(cls, *args, **kwargs):
        return A(42)

    def __init__(self, b_value):
        print("Initialize the new instance of B.")
        self.b_value = b_value
