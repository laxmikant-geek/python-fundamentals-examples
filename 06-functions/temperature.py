"""Small, pure functions: a temperature converter and a discount calculator.

Part of the Python Fundamentals series on GeeksArray.
Run it: python temperature.py
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def apply_discount(price: float, percent: float) -> float:
    """Return the price after a percentage discount."""
    return price * (1 - percent / 100)


def add_tax(price: float, rate: float = 8.0) -> float:
    """Return the price with tax added (default 8%)."""
    return price * (1 + rate / 100)


def final_price(price: float, percent: float) -> float:
    """Apply a discount, then tax, rounded to cents."""
    discounted = apply_discount(price, percent)
    return round(add_tax(discounted), 2)


if __name__ == "__main__":
    print(f"100C = {celsius_to_fahrenheit(100)}F")
    print(f"37C = {celsius_to_fahrenheit(37)}F")

    for sticker in (100, 250):
        print(f"Sticker {sticker} -> final {final_price(sticker, 20)}")
