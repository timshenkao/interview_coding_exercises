# Strategy Design Pattern is a behavioral pattern that enables selecting an algorithm's behavior at runtime.
# It defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# This pattern is useful when you want to switch between different algorithms or behaviors dynamically without modifying
# the context that uses them.

# Benefits of the Strategy Pattern
#     Flexibility: Algorithms can be swapped at runtime, allowing dynamic behavior changes.
#     Encapsulation: Each strategy is encapsulated in its own class, promoting single responsibility and modularity.
#     Extensibility: New strategies can be added without changing the context or client code.
#     Testability: Strategies can be tested independently of the context.
#     Avoids Conditional Logic: Instead of using if-else or switch statements to select behavior, the pattern uses
#         polymorphism.
#
# Drawbacks of the Strategy Pattern
#     Increased Number of Classes: Each algorithm requires a new class, which can increase complexity for simple systems.
#     Client Awareness: The client must know about the available strategies to select the appropriate one.
#     Overhead for Simple Cases: For systems with only one or two algorithms, the pattern may add unnecessary complexity.
#
# When to Use the Strategy Pattern
#     When you need to switch between multiple algorithms or behaviors at runtime.
#     When you want to avoid complex conditional logic in your code.
#     When you need to encapsulate related algorithms in separate classes for better maintainability.
#
# Real-world applications:
#     Sorting algorithms (e.g., choosing between quicksort, mergesort, or bubblesort).
#     Compression algorithms (e.g., ZIP, GZIP, RAR).
#     Payment processing (e.g., different payment gateways with similar interfaces).
#     Text or data formatting.


from abc import ABC, abstractmethod
from typing import Optional

# Abstract Strategy Interface
class TextFormattingStrategy(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass

# Concrete Strategy Classes
class UpperCaseStrategy(TextFormattingStrategy):
    def format(self, text: str) -> str:
        return text.upper()

class LowerCaseStrategy(TextFormattingStrategy):
    def format(self, text: str) -> str:
        return text.lower()

class TitleCaseStrategy(TextFormattingStrategy):
    def format(self, text: str) -> str:
        return text.title()

# Context Class
class TextProcessor:
    def __init__(self, strategy: Optional[TextFormattingStrategy] = None):
        self._strategy = strategy

    def set_strategy(self, strategy: TextFormattingStrategy) -> None:
        self._strategy = strategy
        print(f"TextProcessor: Strategy set to {strategy.__class__.__name__}")

    def format_text(self, text: str) -> str:
        if not self._strategy:
            raise ValueError("No formatting strategy set")
        return self._strategy.format(text)

# Client Code
def main():
    # Create context
    text_processor = TextProcessor()

    # Create strategies
    upper_strategy = UpperCaseStrategy()
    lower_strategy = LowerCaseStrategy()
    title_strategy = TitleCaseStrategy()

    # Test with uppercase strategy
    text_processor.set_strategy(upper_strategy)
    print(text_processor.format_text("Hello, World!"))

    # Test with lowercase strategy
    text_processor.set_strategy(lower_strategy)
    print(text_processor.format_text("Hello, World!"))

    # Test with title case strategy
    text_processor.set_strategy(title_strategy)
    print(text_processor.format_text("hello, world!"))

if __name__ == "__main__":
    main()