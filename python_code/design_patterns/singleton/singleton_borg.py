
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


# Borg Singleton (Monostate)
# Borg pattern ensures that all instances share the same state. This means you can create multiple instances, but they
# all share the same attributes, effectively behaving as if they were the same object in terms of state.
# Key Characteristics of Borg
#       Shared State: All instances of the class share the same state (attributes).
#       Multiple Instances: Unlike Singleton, multiple objects can be created, but they act as one due to shared state.
#       Global Access: Provides a way to access the shared state globally.
#       Lazy Initialization: State is initialized only when needed.
# # The Borg pattern is useful when you want the flexibility of multiple instances but need them to share the same data,
# such as in configuration management or shared resource pools.
# Pros: Simple, flexible (allows multiple instances), and Pythonic.
# Cons: Not thread-safe by default; shared state can lead to unexpected behavior if not carefully managed.
#       But there is thread-safe version

import threading

class ThreadSafeBorg:
    _shared_state = {}
    _lock = threading.Lock()

    def __init__(self):
        with self._lock:
            self.__dict__ = self._shared_state

    def set_attribute(self, key, value):
        with self._lock:
            # Each thread creates its own instance, but they all share the same state, so setting a value in one
            # thread affects all instances.
            self._shared_state[key] = value

    def get_attribute(self, key):
        with self._lock:
            return self._shared_state.get(key)

# Usage in a multithreaded environment
if __name__ == "__main__":
    def configure(name):
        borg = ThreadSafeBorg()
        borg.set_attribute("setting", name)
        print(f"{name}: {borg.get_attribute('setting')}, ID: {id(borg)}")

    threads = []
    for i in range(5):
        t = threading.Thread(target=configure, args=(f"Config-{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()