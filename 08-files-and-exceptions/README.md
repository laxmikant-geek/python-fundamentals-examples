# Files, Exceptions, and Context Managers in Python

Companion code for the article *Files, Exceptions, and Context Managers in Python*.

## What it demonstrates

- `file_io.py` — opening files with `open()` and modes (`r`/`w`/`a`), the `with`
  statement for automatic closing, reading whole-file vs line by line, writing
  text, a CSV round-trip with the `csv` module, and handling a missing file.
- `notes_app.py` — a tiny notes/journal app that appends notes to `notes.txt`
  and reads them back, handling a missing file gracefully and using a custom
  `EmptyNoteError` exception.

## Run it

```bash
python file_io.py

python notes_app.py add "Buy milk"
python notes_app.py add "Call Ada"
python notes_app.py list
```

Requires Python 3.10+. No external dependencies.

📖 **Read the article:** [Files, Exceptions, and Context Managers in Python](https://geeksarray.com/blog/python-fundamentals-files-and-exceptions)

Part 8 of the [Python Fundamentals series](https://geeksarray.com/series/python-fundamentals) on [GeeksArray](https://geeksarray.com).
