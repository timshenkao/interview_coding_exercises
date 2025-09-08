# The Facade Design Pattern is a structural pattern that provides a simplified interface to a complex subsystem.
# It acts as a "front-facing" interface that hides the complexities of the subsystem and makes it easier to use.
# The pattern is useful when you want to provide a unified, high-level interface to a set of classes in a subsystem,
# reducing coupling and improving usability.

# Simplified Interface: The client only needs to call watch_movie() and end_movie() instead of managing each component
# individually.
# Encapsulation: The facade hides the complexity of the subsystem, reducing the chance of errors and improving
# maintainability.
# Loose Coupling: The client doesn’t need to know the details of the subsystem components, reducing dependencies.

# Benefits of the Facade Pattern
#       Simplifies Complex Systems: The facade provides a single point of interaction for complex subsystems, making it
#           easier for clients to use.
#       Improves Maintainability: Changes to the subsystem (e.g., adding a new component) can be handled within the
#           facade without affecting the client code.
#       Reduces Coupling: The client interacts only with the facade, not the subsystem components directly, which
#           reduces dependencies.
#       Promotes Layering: The facade can act as an entry point to a subsystem, enabling layered architectures.

# Drawbacks of the Facade Pattern
#       Limited Flexibility: The facade may oversimplify the subsystem, restricting access to advanced features that
#           some clients might need.
#       Potential for Bloat: If not designed carefully, the facade can become too large, trying to handle too many
#           use cases.
#       Single Point of Failure: If the facade is poorly implemented, it could introduce bugs or performance issues
#           that affect the entire system.


# Real-world applications:
#     Simplifying database access in an ORM (e.g., SQLAlchemy’s high-level APIs).
#     Providing a unified interface for third-party APIs (e.g., a facade for a payment gateway).
#     Simplifying interactions with hardware components, as in the home theater example.


# Subsystem Components
class DVDPlayer:
    def turn_on(self):
        print("DVD Player: Turning on")

    def turn_off(self):
        print("DVD Player: Turning off")

    def play(self, movie: str):
        print(f"DVD Player: Playing '{movie}'")

    def stop(self):
        print("DVD Player: Stopped")

class Projector:
    def turn_on(self):
        print("Projector: Turning on")

    def turn_off(self):
        print("Projector: Turning off")

    def set_input(self, input_source: str):
        print(f"Projector: Setting input to {input_source}")

class SoundSystem:
    def turn_on(self):
        print("Sound System: Turning on")

    def turn_off(self):
        print("Sound System: Turning off")

    def set_volume(self, level: int):
        print(f"Sound System: Setting volume to {level}")

class RoomLights:
    def dim(self, level: int):
        print(f"Room Lights: Dimming to {level}%")

    def turn_on(self):
        print("Room Lights: Turning on")

# Facade Class
class HomeTheaterFacade:
    def __init__(self, dvd_player: DVDPlayer, projector: Projector, sound_system: SoundSystem, lights: RoomLights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie: str):
        print("\nHome Theater: Setting up movie experience...")
        self.lights.dim(10)
        self.projector.turn_on()
        self.projector.set_input("DVD")
        self.sound_system.turn_on()
        self.sound_system.set_volume(50)
        self.dvd_player.turn_on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("\nHome Theater: Shutting down...")
        self.dvd_player.stop()
        self.dvd_player.turn_off()
        self.sound_system.turn_off()
        self.projector.turn_off()
        self.lights.turn_on()

# Client Code
def main():
    # Create subsystem components
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()
    lights = RoomLights()

    # Create facade
    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system, lights)

    # Use facade to watch a movie
    home_theater.watch_movie("Inception")

    # Use facade to end the movie
    home_theater.end_movie()

if __name__ == "__main__":
    main()