from decorators.decorators import timer, debug, do_twice, slow_down
import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@do_twice
def say_whee(name):
    print(f"Whee! {name}")


@do_twice
def say_hello():
    print("Hello!")


@timer
def return_greeting(name):
    time.sleep(2)
    print("Creating greeting")
    return f"Hi {name}"


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff")
    else:
        print(from_number)
        countdown(from_number-1)

# say_whee("Anthony")
# say_hello()

# hi_anthony = return_greeting("Anthony")
# print(hi_anthony)

# make_greeting('Anthony', 42)
countdown(100)