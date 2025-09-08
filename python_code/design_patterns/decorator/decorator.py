# Decorator pattern is a structural design pattern that allows behavior to be added to an object dynamically without
# modifying its code. It’s particularly useful for extending functionalities in a flexible and reusable way.

# Key Characteristics of Decorator
#     Purpose: Adds responsibilities to objects in a dynamic and transparent manner.
#     Use Case: When you need to extend an object’s functionality without subclassing, or when you want to combine
#         multiple optional behaviors.
#     Components:
#         Component: Defines the interface for objects that can have responsibilities added.
#         Concrete Component: The class to which additional responsibilities are added.
#         Decorator: Implements the component interface and contains a reference to a component object.
#         Concrete Decorator: Adds specific responsibilities to the component.
#     Benefits: Promotes flexibility, adheres to the Open/Closed Principle, and allows runtime behavior composition.

# This is not thread-safe implementation
# If the decorated object involves shared resources (e.g., a counter for coffee orders), you can add Lock

from abc import ABC, abstractmethod

# Component: Interface for coffee objects
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Component: Base coffee types
class Espresso(Coffee):
    def get_description(self) -> str:
        return "Espresso"

    def get_cost(self) -> float:
        return 2.50

class Latte(Coffee):
    def get_description(self) -> str:
        return "Latte"

    def get_cost(self) -> float:
        return 3.00

# Decorator: Abstract decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Decorators: Add specific ingredients
class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, Sugar"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.20

class WhippedCreamDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, Whipped Cream"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75

# Usage
if __name__ == "__main__":
    # Order an Espresso with Milk and Sugar
    espresso = Espresso()
    espresso_with_milk = MilkDecorator(espresso)
    espresso_with_milk_sugar = SugarDecorator(espresso_with_milk)

    print(f"Order: {espresso_with_milk_sugar.get_description()}")
    print(f"Cost: ${espresso_with_milk_sugar.get_cost():.2f}")

    # Order a Latte with Whipped Cream
    latte = Latte()
    latte_with_cream = WhippedCreamDecorator(latte)

    print(f"\nOrder: {latte_with_cream.get_description()}")
    print(f"Cost: ${latte_with_cream.get_cost():.2f}")