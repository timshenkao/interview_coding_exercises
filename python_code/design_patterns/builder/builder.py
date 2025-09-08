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


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

# Product
@dataclass
class Computer:
    cpu: Optional[str] = None
    ram: Optional[int] = None  # in GB
    storage: Optional[int] = None  # in GB
    gpu: Optional[str] = None
    power_supply: Optional[int] = None  # in Watts

    def __str__(self) -> str:
        return (f"Computer [CPU: {self.cpu}, RAM: {self.ram}GB, "
                f"Storage: {self.storage}GB, GPU: {self.gpu}, "
                f"Power Supply: {self.power_supply}W]")

# Builder Interface
class ComputerBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_cpu(self, cpu: str) -> None:
        pass

    @abstractmethod
    def set_ram(self, ram: int) -> None:
        pass

    @abstractmethod
    def set_storage(self, storage: int) -> None:
        pass

    @abstractmethod
    def set_gpu(self, gpu: str) -> None:
        pass

    @abstractmethod
    def set_power_supply(self, power_supply: int) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Computer:
        pass

# Concrete Builder for Gaming PC
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> None:
        self._computer.cpu = cpu

    def set_ram(self, ram: int) -> None:
        self._computer.ram = ram

    def set_storage(self, storage: int) -> None:
        self._computer.storage = storage

    def set_gpu(self, gpu: str) -> None:
        self._computer.gpu = gpu

    def set_power_supply(self, power_supply: int) -> None:
        self._computer.power_supply = power_supply

    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()  # Reset for next build
        return computer

# Concrete Builder for Office PC
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> None:
        self._computer.cpu = cpu

    def set_ram(self, ram: int) -> None:
        self._computer.ram = ram

    def set_storage(self, storage: int) -> None:
        self._computer.storage = storage

    def set_gpu(self, gpu: str) -> None:
        self._computer.gpu = gpu

    def set_power_supply(self, power_supply: int) -> None:
        self._computer.power_supply = power_supply

    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

# Director
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def construct_gaming_pc(self) -> None:
        self._builder.set_cpu("Intel i9-13900K")
        self._builder.set_ram(32)
        self._builder.set_storage(1000)
        self._builder.set_gpu("NVIDIA RTX 4090")
        self._builder.set_power_supply(850)

    def construct_office_pc(self) -> None:
        self._builder.set_cpu("Intel i5-12400")
        self._builder.set_ram(16)
        self._builder.set_storage(512)
        self._builder.set_gpu("Integrated")
        self._builder.set_power_supply(400)

    def get_computer(self) -> Computer:
        return self._builder.get_result()

# Usage
if __name__ == "__main__":
    # Create gaming PC
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    director.construct_gaming_pc()
    gaming_pc = director.get_computer()
    print("Gaming PC:", gaming_pc)

    # Create office PC
    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    director.construct_office_pc()
    office_pc = director.get_computer()
    print("Office PC:", office_pc)

    # Custom configuration without director
    custom_builder = GamingComputerBuilder()
    custom_builder.set_cpu("AMD Ryzen 9 7950X")
    custom_builder.set_ram(64)
    custom_builder.set_storage(2000)
    custom_pc = custom_builder.get_result()
    print("Custom PC:", custom_pc)