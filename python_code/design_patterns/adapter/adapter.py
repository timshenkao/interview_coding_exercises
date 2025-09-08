# Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to work together by
# wrapping one interface to make it compatible with another.

# Key Characteristics of Adapter
#     Purpose: Converts the interface of a class into another interface that a client expects.
#     Use Case: When integrating legacy systems, third-party APIs, or classes with incompatible interfaces.
#     Components:
#         Target: The interface the client expects.
#         Adaptee: The existing class with an incompatible interface.
#         Adapter: The class that bridges the Target and Adaptee.

# Types:
#     Object Adapter: Uses composition (preferred in Python for flexibility).
#     Class Adapter: Uses inheritance (less common in Python due to multiple inheritance complexities).

# Real-World Use Case: Payment Gateway Integration


class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"

class Cat:
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"

class Human:
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"

class Car:
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)

class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """
    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


if __name__ == "__main__":
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda : car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A", obj.name, "goes", obj.make_noise()) 