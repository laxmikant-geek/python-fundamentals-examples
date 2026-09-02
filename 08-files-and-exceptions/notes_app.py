"""A tiny notes/journal app that appends lines to a file and reads them back.

Demonstrates: append mode, line-by-line reads, handling a missing file
gracefully, raising exceptions, and a custom exception type.

Run it:
    python notes_app.py add "Buy milk"
    python notes_app.py list
"""

import sys
from pathlib import Path

NOTES = Path("notes.txt")


class EmptyNoteError(Exception):
    """Raised when someone tries to add a blank note."""


def add_note(text):
    """Append a single note as one line."""
    if not text.strip():
        raise EmptyNoteError("A note cannot be empty.")
    with open(NOTES, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")


def read_notes():
    """Return all notes as a list, or [] if the file does not exist yet."""
    try:
        with open(NOTES, "r", encoding="utf-8") as f:
            return [line.rstrip() for line in f]
    except FileNotFoundError:
        return []  # no notes yet is not an error


def main(argv):
    if len(argv) < 2:
        print("Usage: python notes_app.py [add <text> | list]")
        return

    command = argv[1]

    if command == "add":
        try:
            add_note(" ".join(argv[2:]))
        except EmptyNoteError as exc:
            print(f"Could not add note: {exc}")
        else:
            print("Added note.")
    elif command == "list":
        notes = read_notes()
        if not notes:
            print("No notes yet.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main(sys.argv)
