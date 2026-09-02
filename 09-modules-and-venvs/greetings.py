# greetings.py — a small, importable module.
# Define reusable functions at the top level so other files can import them.


def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def shout(name):
    """Return the greeting in uppercase."""
    return greet(name).upper()


# This runs only when the file is executed directly (python greetings.py),
# not when it is imported by another module.
if __name__ == "__main__":
    print(greet("Ada"))
    print(shout("Ada"))
