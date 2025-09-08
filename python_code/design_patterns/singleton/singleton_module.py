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


# Module-Based Singleton (Pythonic Approach)
# In Python, a module itself can act as a Singleton because it’s imported only once.
# Python modules are loaded once and cached in sys.modules, making them natural Singletons.
# The get_config_manager function ensures lazy initialization.
# Pros: Simple, Pythonic, thread-safe (Python’s module import system handles concurrency).
# Cons: Less explicit than class-based Singletons; not suitable if you need class-based features like inheritance.


# file config_manager.py
_config = None

def get_config_manager():
    global _config
    if _config is None:
        _config = {"db_host": "localhost", "port": 5432}
    return _config


# Usage in another file
if __name__ == "__main__":
    from config_manager import get_config_manager

    config1 = get_config_manager()
    config1["db_host"] = "127.0.0.1"

    config2 = get_config_manager()
    print(config2["db_host"])  # Output: 127.0.0.1
    print(config1 is config2)  # Output: True

