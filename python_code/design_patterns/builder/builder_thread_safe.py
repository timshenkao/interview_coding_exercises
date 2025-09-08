# Builder pattern is a creational design pattern that separates the construction of a complex object from its
# representation, allowing the same construction process to create different representations.

# Key Characteristics of Builder
#     Purpose: Constructs complex objects step-by-step, providing control over the construction process.
#     Use Case: When an object has many optional or required components, or when the construction process needs to be
#           flexible or reusable.
#     Components:
#         Product: The complex object being built.
#         Builder: Defines the interface for building parts of the product.
#         Concrete Builder: Implements the builder interface to construct specific parts.
#         Director: Orchestrates the construction process using a builder.
#     Benefits: Encapsulates construction logic, promotes immutability of the product, and allows for varied
#           configurations.

# If the builder needs to be used in a multithreaded environment (e.g., constructing shared resources), you can add
# thread safety.


import threading
from dataclasses import dataclass
from typing import Optional

# Product
@dataclass
class Computer:
    cpu: Optional[str] = None
    ram: Optional[int] = None

    def __str__(self) -> str:
        return f"Computer [CPU: {self.cpu}, RAM: {self.ram}GB]"

# Thread-Safe Builder
class ThreadSafeComputerBuilder:
    def __init__(self):
        self._computer = Computer()
        self._lock = threading.Lock()

    def set_cpu(self, cpu: str) -> None:
        with self._lock:
            self._computer.cpu = cpu

    def set_ram(self, ram: int) -> None:
        with self._lock:
            self._computer.ram = ram

    def get_result(self) -> Computer:
        with self._lock:
            computer = self._computer
            self._computer = Computer()  # Reset for next build
            return computer

# Usage
if __name__ == "__main__":
    def build_computer(builder: ThreadSafeComputerBuilder, cpu: str, ram: int):
        builder.set_cpu(cpu)
        builder.set_ram(ram)
        computer = builder.get_result()
        print(f"Thread {threading.current_thread().name}: {computer}")

    builder = ThreadSafeComputerBuilder()
    threads = []
    for i in range(3):
        t = threading.Thread(target=build_computer, args=(builder, f"CPU-{i}", 16 + i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()