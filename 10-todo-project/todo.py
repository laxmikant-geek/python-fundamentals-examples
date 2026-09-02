"""A small command-line to-do list that ties the series together.

It uses functions, a list of dictionaries, JSON file I/O, and exception
handling — the building blocks from earlier parts of the series.

Run it:  python todo.py add "Write the finale post"
         python todo.py list
         python todo.py done 1
"""
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


# --- Core logic (pure functions, easy to test) -----------------------------

def add_task(tasks, title):
    """Return a new list with a task appended. Raises on an empty title."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    next_id = max((t["id"] for t in tasks), default=0) + 1
    return tasks + [{"id": next_id, "title": title, "done": False}]


def complete_task(tasks, task_id):
    """Return a new list with the matching task marked done."""
    if not any(t["id"] == task_id for t in tasks):
        raise KeyError(f"No task with id {task_id}.")
    return [
        {**t, "done": True} if t["id"] == task_id else t
        for t in tasks
    ]


def format_tasks(tasks):
    """Return a printable string for the whole list."""
    if not tasks:
        return "No tasks yet. Add one with:  python todo.py add \"...\""
    lines = []
    for t in tasks:
        mark = "x" if t["done"] else " "
        lines.append(f"[{mark}] {t['id']}. {t['title']}")
    return "\n".join(lines)


# --- Persistence -----------------------------------------------------------

def load_tasks(path=DATA_FILE):
    """Load tasks from JSON, returning [] if the file is missing."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: tasks file is corrupt; starting fresh.")
        return []


def save_tasks(tasks, path=DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


# --- Command-line glue -----------------------------------------------------

def main(argv):
    if not argv:
        print(__doc__)
        return
    command, *rest = argv
    tasks = load_tasks()

    if command == "add":
        tasks = add_task(tasks, " ".join(rest))
        save_tasks(tasks)
        print("Added.")
    elif command == "done":
        tasks = complete_task(tasks, int(rest[0]))
        save_tasks(tasks)
        print("Marked done.")
    elif command == "list":
        print(format_tasks(tasks))
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main(sys.argv[1:])
