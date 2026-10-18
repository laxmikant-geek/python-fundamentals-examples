# 09 — Modules, Packages, and Virtual Environments

Companion code for the article *Modules, Packages, and Virtual Environments in Python*.

## What it demonstrates

- `greetings.py` — a small, importable module with reusable functions and an `if __name__ == "__main__":` guard.
- `main.py` — imports our `greetings` module plus standard-library modules (`random`, `datetime`) and runs behind the same guard.
- `requirements.txt` — where you record third-party dependencies (this demo uses only the standard library).

## Run it

```bash
python greetings.py   # runs the module's own demo (guard fires)
python main.py        # imports greetings; its demo stays silent
```

## Try a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

Use `python3` instead of `python` on macOS/Linux if needed. Requires Python 3.10+.

Part 9 of the [Python Fundamentals series](https://geeksarray.com/series/python-fundamentals) on [GeeksArray](https://geeksarray.com).
