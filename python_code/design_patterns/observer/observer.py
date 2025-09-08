# Observer Design Pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when
# one object (the subject) changes its state, all its dependent objects (observers) are notified and updated
# automatically. This pattern is useful for implementing event-driven systems where
# multiple objects need to react to changes in another object.


# Benefits of the Observer Pattern
#     Decoupling: The subject and observers are loosely coupled, allowing changes to either without affecting the other.
#     Extensibility: New observers can be added without modifying the subject.
#     Dynamic Behavior: Observers can be added or removed at runtime, making the system flexible.
#     Event-Driven Design: The pattern supports event-driven systems, where changes in one object trigger actions in
#         others.
#
# Drawbacks of the Observer Pattern
#     Memory Leaks: If observers are not properly removed, they can remain in memory, especially in long-running systems.
#     Performance Overhead: Notifying many observers can be slow if the list is large or updates are frequent.
#     Complexity in Updates: If observers modify the subject during an update, it can lead to unexpected behavior
#             (e.g., infinite loops).
#     Data Overhead: In the push model, the subject sends all data to observers, even if they don’t need it (a pull model
#         could mitigate this).


# When to Use the Observer Pattern
#     When multiple objects need to react to changes in another object’s state.
#     When you want a loosely coupled system where objects can subscribe or unsubscribe dynamically.
#     When implementing event-driven systems, such as GUI frameworks or real-time data feeds.

# Real-world applications:
#     GUI frameworks (e.g., button click listeners in Tkinter or PyQt).
#     Real-time data feeds (e.g., stock price updates to multiple displays).
#     Pub/sub systems (e.g., message queues like RabbitMQ or Kafka)


# Requirements:
# The weather station maintains a list of observers and notifies them when measurements change.
# Observers can subscribe or unsubscribe from the weather station.
# Each observer displays data differently (e.g., current conditions or statistical summaries).
from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

# Abstract Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

# Subject (Weather Station)
class WeatherStation:
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
        print(f"Observer {observer.__class__.__name__} registered")

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Observer {observer.__class__.__name__} removed")

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        print(f"\nWeather Station: New measurements - Temp: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure}hPa")
        self.notify_observers()

# Concrete Observers
@dataclass
class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Current Conditions: {temperature}°C, {humidity}% humidity, {pressure}hPa pressure")

@dataclass
class StatisticsDisplay(Observer):
    temperatures: List[float] = None

    def __post_init__(self):
        self.temperatures = []

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperatures.append(temperature)
        avg_temp = sum(self.temperatures) / len(self.temperatures) if self.temperatures else 0.0
        max_temp = max(self.temperatures) if self.temperatures else 0.0
        min_temp = min(self.temperatures) if self.temperatures else 0.0
        print(f"Statistics: Avg Temp: {avg_temp:.2f}°C, Max Temp: {max_temp:.2f}°C, Min Temp: {min_temp:.2f}°C")

# Client Code
def main():
    # Create subject
    weather_station = WeatherStation()

    # Create observers
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()

    # Register observers
    weather_station.register_observer(current_display)
    weather_station.register_observer(stats_display)

    # Simulate new weather measurements
    weather_station.set_measurements(25.5, 65.0, 1013.2)
    weather_station.set_measurements(26.0, 70.0, 1012.8)

    # Remove one observer
    weather_station.remove_observer(current_display)

    # Simulate another measurement
    weather_station.set_measurements(24.8, 68.0, 1014.0)

if __name__ == "__main__":
    main()