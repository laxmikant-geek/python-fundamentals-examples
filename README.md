# Python Fundamentals — Examples

Companion source code for the **Python Fundamentals** series on
[GeeksArray](https://geeksarray.com) — [read the series](https://geeksarray.com/series/python-fundamentals). Each folder holds the runnable examples for one
article in the series, so you can read a post and run the exact code alongside it.

Everything here targets **Python 3.10+** and uses only the standard library
(the only third-party tool is `pytest`, used in Part 10).

## Contents

| # | Folder | Article |
|---|--------|---------|
| 1 | [`01-getting-started`](01-getting-started) | Getting Started with Python: Install, Run, and Your First Program |
| 2 | [`02-variables-and-types`](02-variables-and-types) | Variables, Numbers, and Types in Python |
| 3 | [`03-strings`](03-strings) | Working with Strings and Text in Python |
| 4 | [`04-collections`](04-collections) | Python Collections: Lists, Tuples, Sets, and Dictionaries |
| 5 | [`05-control-flow`](05-control-flow) | Control Flow in Python: Conditionals and Loops |
| 6 | [`06-functions`](06-functions) | Functions in Python: Arguments, Return Values, and Scope |
| 7 | [`07-oop`](07-oop) | Object-Oriented Programming in Python |
| 8 | [`08-files-and-exceptions`](08-files-and-exceptions) | Files, Exceptions, and Context Managers in Python |
| 9 | [`09-modules-and-venvs`](09-modules-and-venvs) | Modules, Packages, and Virtual Environments in Python |
| 10 | [`10-todo-project`](10-todo-project) | Testing Your Code and Building Your First Python Project |

## Running the examples

```bash
# check your Python version (needs 3.10 or newer)
python --version

# run any example
cd 01-getting-started
python greet.py
```

Part 10 includes tests:

```bash
cd 10-todo-project
python -m pip install pytest
pytest
```

## About

Written by the team at GeeksArray — *Connect · Develop · Succeed*.
Read the full series at <https://geeksarray.com/series/python-fundamentals>.
