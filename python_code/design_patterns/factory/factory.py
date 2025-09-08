# Factory Design Pattern is a creational pattern that provides a way to create objects without specifying the exact
# class of object that will be created. It encapsulates object creation logic in a separate method or class,
# promoting loose coupling and enhancing flexibility. This pattern is particularly useful when the type of object to
# instantiate is determined at runtime or when you want to centralize object creation logic.

# Benefits of the Factory Pattern
#     Centralized Object Creation: All object creation logic is in one place, making it easier to maintain and modify.
#     Decoupling: The client code depends only on the abstract interface and the factory, not on concrete classes.
#     Extensibility: New classes can be added with minimal changes to the factory and no changes to the client code.
#     Improved Readability: Using a factory makes the code more expressive, as the client doesn’t need to deal with
#         instantiation details.
#
# Drawbacks of the Factory Pattern
#     Increased Complexity: For simple systems, a factory might add unnecessary overhead compared to direct instantiation.
#     Single Point of Maintenance: The factory must be updated whenever a new subclass is added, which can become
#         cumbersome if many types are supported.
#     Potential for Overuse: Overusing factories for trivial cases can lead to bloated code.


# When to Use the Factory Pattern
#     When the type of object to create depends on runtime conditions (e.g., user input, configuration, or data).
#     When you want to centralize object creation logic to improve maintainability.
#     When you need to decouple client code from concrete classes.
#
# Real-world applications:
#     Creating database connections (e.g., SQL vs. NoSQL based on configuration).
#     Instantiating UI components (e.g., buttons or windows for different operating systems).
#     Handling different file formats (e.g., JSON, XML, CSV parsers).


from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Optional

# Enum for payment types
class PaymentType(Enum):
    CREDIT_CARD = auto()
    PAYPAL = auto()
    BANK_TRANSFER = auto()

# Abstract base class for payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

# Concrete payment method classes
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing credit card payment of ${amount:.2f}"

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing PayPal payment of ${amount:.2f}"

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing bank transfer payment of ${amount:.2f}"

# Factory class
class PaymentFactory:
    @staticmethod
    def create_payment_method(payment_type: PaymentType) -> Optional[PaymentMethod]:
        if payment_type == PaymentType.CREDIT_CARD:
            return CreditCardPayment()
        elif payment_type == PaymentType.PAYPAL:
            return PayPalPayment()
        elif payment_type == PaymentType.BANK_TRANSFER:
            return BankTransferPayment()
        else:
            return None

# Client code
def main():
    # Create factory
    factory = PaymentFactory()

    # Process a credit card payment
    payment_method = factory.create_payment_method(PaymentType.CREDIT_CARD)
    if payment_method:
        print(payment_method.process_payment(100.50))

    # Process a PayPal payment
    payment_method = factory.create_payment_method(PaymentType.PAYPAL)
    if payment_method:
        print(payment_method.process_payment(75.25))

    # Process a bank transfer payment
    payment_method = factory.create_payment_method(PaymentType.BANK_TRANSFER)
    if payment_method:
        print(payment_method.process_payment(200.00))

if __name__ == "__main__":
    main()