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

# Decorators are applied in reverse order (bottom-up), so timing_decorator runs first, then logging_decorator.
# Use of functools.wraps: Preserves the original function’s metadata (e.g., __name__).
# Pros: Pythonic, concise, and ideal for function-based extensions.
#     Cons: Limited to functions; less flexible for complex object hierarchies.


import time
import functools
from typing import Callable

# Decorator: Logging
def logging_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Decorator: Timing
def timing_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Concrete Component: A function to decorate
@logging_decorator
@timing_decorator
def compute_sum(n: int) -> int:
    return sum(range(n))

# Usage
if __name__ == "__main__":
    result = compute_sum(1000000)
    print(f"Final result: {result}")