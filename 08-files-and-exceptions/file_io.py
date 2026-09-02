"""Reading and writing files safely, plus a taste of the csv module.

Run it:  python file_io.py
"""

import csv
from pathlib import Path


def write_and_read_text():
    """Write a file with `with`, then read it back two ways."""
    path = Path("greeting.txt")

    # "w" creates or truncates. The `with` block auto-closes the file.
    with open(path, "w", encoding="utf-8") as f:
        f.write("Hello, file!\n")
        f.write("Second line.\n")

    # Whole-file read: fine for small files.
    with open(path, "r", encoding="utf-8") as f:
        print("--- read() ---")
        print(f.read())

    # Line-by-line: memory-friendly for big files.
    with open(path, "r", encoding="utf-8") as f:
        print("--- line by line ---")
        for line in f:
            print(line.rstrip())  # rstrip() drops the trailing newline


def append_text():
    """Append does not erase what is already there."""
    with open("greeting.txt", "a", encoding="utf-8") as f:
        f.write("Appended later.\n")


def csv_roundtrip():
    """Use the csv module instead of splitting on commas by hand."""
    # newline="" lets the csv module control line endings.
    with open("people.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "role"])
        writer.writerow(["Ada", "engineer"])
        writer.writerow(["Grace", "admiral"])

    with open("people.csv", "r", newline="", encoding="utf-8") as f:
        print("--- csv rows ---")
        for row in csv.reader(f):
            print(row)  # each row is a list of strings


def read_missing_safely():
    """A missing file is a normal case, not a crash."""
    try:
        with open("does-not-exist.txt", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""  # sensible default


if __name__ == "__main__":
    write_and_read_text()
    append_text()
    csv_roundtrip()
    print("--- missing file ---")
    print(repr(read_missing_safely()))
