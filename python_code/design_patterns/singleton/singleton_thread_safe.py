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


# Thread-Safe Singleton with Locking
# To make the Singleton thread-safe, we can use a lock from the threading module.
# Pros: Thread-safe, suitable for concurrent environments.
# Cons: Slightly more complex due to locking; minimal performance overhead from locking.

import threading


def create_instance(name):
    singleton = SingletonThreadSafe()
    singleton.value = name
    print(f"{name}: {singleton.value}, ID: {id(singleton)}")


class SingletonThreadSafe:
    _instance = None
    # The _lock ensures that only one thread can create the instance at a time.
    _lock = threading.Lock()  # Lock for thread safety

    def __new__(cls):
        # block synchronizes access to the _instance check and creation.
        # This prevents race conditions in multithreaded applications.
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.value = None


# Usage in a multithreaded environment
if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_instance, args=(f"Thread-{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
