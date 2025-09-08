# State Design Pattern is a behavioral pattern that allows an object to alter its behavior when its internal state
# changes. It encapsulates state-specific behavior into separate classes and delegates the behavior to the current state
# object, making the system more modular and easier to extend. This pattern is useful when an object’s behavior depends
# on its state, and the state transitions need to be managed cleanly.


# Benefits of the State Pattern
#     Modularity: Each state’s behavior is encapsulated in a separate class, adhering to the Single Responsibility
#         Principle.
#     Extensibility: New states can be added without modifying the context or existing states.
#     Eliminates Conditional Logic: Instead of using complex if-else or switch statements, the pattern uses polymorphism
#         to handle state-specific behavior.
#     Clear State Transitions: The pattern makes state transitions explicit and manageable within state classes.

# Drawbacks of the State Pattern
#     Increased Number of Classes: Each state requires a new class, which can increase complexity for systems with many
#           states.
#     Overhead for Simple Systems: For systems with few states or simple behavior, the pattern may add unnecessary
#           complexity.
#     State Management: Managing state transitions can become complex if states have intricate dependencies.

# When to Use the State Pattern
#     When an object’s behavior depends on its state, and the state changes frequently.
#     When you want to avoid complex conditional logic for state-dependent behavior.
#     When you need to manage state transitions in a clean and extensible way.
#
# Real-world applications:
#     Workflow systems (e.g., order processing: Pending, Shipped, Delivered).
#     UI components (e.g., button states: Enabled, Disabled, Hover).
#     Game character states (e.g., Idle, Running, Jumping).


from abc import ABC, abstractmethod
from typing import Optional

# Abstract State Interface
class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine: 'VendingMachine') -> None:
        pass

    @abstractmethod
    def select_product(self, machine: 'VendingMachine') -> None:
        pass

    @abstractmethod
    def dispense(self, machine: 'VendingMachine') -> None:
        pass

# Concrete State Classes
class NoCoinState(VendingMachineState):
    def insert_coin(self, machine: 'VendingMachine') -> None:
        print("NoCoinState: Coin inserted")
        machine.set_state(HasCoinState())

    def select_product(self, machine: 'VendingMachine') -> None:
        print("NoCoinState: Cannot select product, please insert a coin")

    def dispense(self, machine: 'VendingMachine') -> None:
        print("NoCoinState: Cannot dispense, please insert a coin")

class HasCoinState(VendingMachineState):
    def insert_coin(self, machine: 'VendingMachine') -> None:
        print("HasCoinState: Coin already inserted")

    def select_product(self, machine: 'VendingMachine') -> None:
        if machine.stock > 0:
            print("HasCoinState: Product selected")
            machine.set_state(DispensingState())
        else:
            print("HasCoinState: Out of stock")
            machine.set_state(OutOfStockState())

    def dispense(self, machine: 'VendingMachine') -> None:
        print("HasCoinState: Cannot dispense, please select a product")

class DispensingState(VendingMachineState):
    def insert_coin(self, machine: 'VendingMachine') -> None:
        print("DispensingState: Cannot insert coin while dispensing")

    def select_product(self, machine: 'VendingMachine') -> None:
        print("DispensingState: Cannot select product while dispensing")

    def dispense(self, machine: 'VendingMachine') -> None:
        print("DispensingState: Dispensing product")
        machine.stock -= 1
        if machine.stock > 0:
            machine.set_state(NoCoinState())
        else:
            machine.set_state(OutOfStockState())

class OutOfStockState(VendingMachineState):
    def insert_coin(self, machine: 'VendingMachine') -> None:
        print("OutOfStockState: Cannot insert coin, machine is out of stock")

    def select_product(self, machine: 'VendingMachine') -> None:
        print("OutOfStockState: Cannot select product, machine is out of stock")

    def dispense(self, machine: 'VendingMachine') -> None:
        print("OutOfStockState: Cannot dispense, machine is out of stock")

# Context Class
class VendingMachine:
    def __init__(self, stock: int):
        self.stock = stock
        self._state: Optional[VendingMachineState] = None
        self.set_state(NoCoinState())

    def set_state(self, state: VendingMachineState) -> None:
        self._state = state
        print(f"VendingMachine: Transitioned to {state.__class__.__name__}")

    def insert_coin(self) -> None:
        if self._state:
            self._state.insert_coin(self)

    def select_product(self) -> None:
        if self._state:
            self._state.select_product(self)

    def dispense(self) -> None:
        if self._state:
            self._state.dispense(self)

# Client Code
def main():
    # Create vending machine with 2 products in stock
    vending_machine = VendingMachine(stock=2)

    # Test scenario
    print("\nScenario: Insert coin, select product, dispense")
    vending_machine.insert_coin()
    vending_machine.select_product()
    vending_machine.dispense()

    print("\nScenario: Try to dispense without selecting")
    vending_machine.insert_coin()
    vending_machine.dispense()

    print("\nScenario: Select and dispense last product")
    vending_machine.select_product()
    vending_machine.dispense()

    print("\nScenario: Try to insert coin when out of stock")
    vending_machine.insert_coin()

if __name__ == "__main__":
    main()