"""Interactive tip calculator.

Demonstrates type conversion (input() returns str), arithmetic,
augmented assignment, and f-string formatting.

Run it: python calculator.py
"""

# Constant by convention — UPPER_CASE means "do not reassign".
DEFAULT_TIP_PERCENT = 15


def read_float(prompt: str, default: float) -> float:
    """Read a float from the user, falling back to a default on blank/invalid input."""
    raw = input(prompt).strip()
    if raw == "":
        return default
    try:
        return float(raw)  # input() gives a str; convert it
    except ValueError:
        print(f"  Not a number, using {default}")
        return default


def main() -> None:
    print("=== Tip Calculator ===")
    bill = read_float("Bill amount: ", 84.50)
    tip_percent = read_float(f"Tip % [{DEFAULT_TIP_PERCENT}]: ", DEFAULT_TIP_PERCENT)
    people = int(read_float("Number of people [1]: ", 1))
    people = max(people, 1)  # never divide by zero

    tip = bill * tip_percent / 100
    total = bill + tip
    per_person = total / people

    print()
    print(f"Tip:       {tip:.2f}")
    print(f"Total:     {total:.2f}")
    print(f"Each pays: {per_person:.2f}")


if __name__ == "__main__":
    main()
