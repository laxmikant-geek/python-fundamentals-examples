# To-Do Project — capstone

A tiny command-line to-do list that ties the whole series together: functions,
a list of dictionaries, JSON file persistence, and exception handling, all with
tests.

## What it demonstrates

- **Pure core functions** (`add_task`, `complete_task`, `format_tasks`) that are
  easy to test.
- **Persistence** to a JSON file with `load_tasks` / `save_tasks`.
- **Exception handling** for empty titles, unknown ids, and a missing/corrupt
  file.
- **pytest** tests for the core logic in `test_todo.py`.

## Run it

```bash
python todo.py add "Write the finale post"
python todo.py list
python todo.py done 1
```

## Run the tests

```bash
pip install pytest
pytest
```

Part of the Python Fundamentals series on GeeksArray.
