"""Core function concepts: parameters, returns, defaults, *args/**kwargs.

Part of the Python Fundamentals series on GeeksArray.
Run it: python functions_demo.py
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    """Build a greeting, defaulting to 'Hello'."""
    return f"{greeting}, {name}!"


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return the smallest and largest values as a tuple."""
    return min(numbers), max(numbers)


def total(*numbers: float) -> float:
    """Sum any number of positional arguments (*args)."""
    return sum(numbers)


def describe(**details: str) -> None:
    """Print any number of keyword arguments (**kwargs)."""
    for key, value in details.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print(add(2, 3))
    print(greet("Ada"))
    print(greet("Ada", greeting="Hi"))

    low, high = min_max([4, 9, 1, 7])
    print(f"low={low}, high={high}")

    print(total(10, 20, 30, 40))
    describe(name="Ada", role="engineer")
