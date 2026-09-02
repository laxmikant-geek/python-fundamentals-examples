"""Clean messy input and print an aligned report table.

Part of the Python Fundamentals series on GeeksArray.
Run it: python text_report.py
"""

# Each raw line is intentionally messy: extra spaces and mixed case.
RAW_LINES = [
    "  ada Lovelace , engineer , 92.4 ",
    "grace HOPPER , admiral , 88.15 ",
    " alan turing , researcher , 99.5",
]


def parse_line(raw: str) -> tuple[str, str, float]:
    """Split a comma-separated line, strip and normalise each field."""
    name, role, score = [part.strip() for part in raw.split(",")]
    return name.title(), role.capitalize(), float(score)


def format_row(name: str, role: str, score: float) -> str:
    """Build one aligned report line using f-string specifiers."""
    return f"{name:<15} | {role:<12} | {score:6.2f}"


def main() -> None:
    header = f"{'Name':<15} | {'Role':<12} | {'Score':>6}"
    print(header)
    print("-" * len(header))

    for raw in RAW_LINES:
        name, role, score = parse_line(raw)
        print(format_row(name, role, score))


if __name__ == "__main__":
    main()
