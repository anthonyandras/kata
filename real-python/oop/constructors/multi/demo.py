class DemoClass:
    @classmethod
    def class_method(cls):
        """
            instance is not required to call this, returns instance of the class implicitly
            this is considered an alternative constructor
        """
        print(f"A class method from {cls.__name__}!")


if __name__ == '__main__':
    DemoClass.class_method()
    demo = DemoClass()
    demo.class_method()