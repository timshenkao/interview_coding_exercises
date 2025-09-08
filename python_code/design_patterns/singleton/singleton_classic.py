# The Singleton design pattern ensures a class has only one instance and provides a global point of access to it. It's
# useful when you need exactly one object to coordinate actions across a system, like a configuration manager or a
# database connection pool.

# Key Characteristics of Singleton
#     Single Instance: Only one instance of the class exists.
#     Global Access: A mechanism to access the instance globally.
#     Lazy Initialization: The instance is created only when needed.

# Real-World Use Case: Database Connection Pool

# Use Cases:
#     Managing shared resources (e.g., database connections, logging systems).
#     Global configuration settings.
#     Caching mechanisms.
# Avoid When:
#     The class needs multiple instances or state variations.
#     Testing becomes difficult (Singletons can complicate unit tests due to global state).
#     You need flexibility for future extensions (e.g., multiple configurations).


# Classic Singleton with __new__
# Subsequent calls to Singleton() return the same _instance.
# Pros: Simple and explicit control over instance creation.
# Cons: Not thread-safe (in multithreaded environments, multiple instances could be created if threads access
# __new__ simultaneously).
class SingletonClassic:
    _instance = None  # Class-level variable to store the single instance

    # __new__ is called before __init__ and is responsible for creating the instance.
    def __new__(cls):
        # We check if _instance is None. If it is, we create a new instance using super().__new__(cls).
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # The __init__ method is guarded with _initialized to prevent reinitialization, as __init__ is called every time
    # Singleton() is invoked.
    def __init__(self):
        # Initialize only if not already initialized
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.value = None  # Example attribute

# Usage
if __name__ == "__main__":
    s1 = SingletonClassic()
    s1.value = "Instance 1"
    s2 = SingletonClassic()

    print(s1.value)  # Output: Instance 1
    print(s2.value)  # Output: Instance 1
    print(s1 is s2)  # Output: True (same instance)