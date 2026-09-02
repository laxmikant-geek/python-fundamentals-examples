"""Tests for the to-do core logic, run with: pytest"""
import pytest

from todo import add_task, complete_task, format_tasks


def test_add_task_assigns_first_id():
    tasks = add_task([], "Learn testing")
    assert tasks == [{"id": 1, "title": "Learn testing", "done": False}]


def test_add_task_increments_id():
    tasks = add_task([], "one")
    tasks = add_task(tasks, "two")
    assert [t["id"] for t in tasks] == [1, 2]


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_complete_task_marks_done():
    tasks = add_task([], "ship it")
    tasks = complete_task(tasks, 1)
    assert tasks[0]["done"] is True


def test_complete_task_unknown_id_raises():
    with pytest.raises(KeyError):
        complete_task([], 99)


def test_format_tasks_shows_marks():
    tasks = complete_task(add_task(add_task([], "a"), "b"), 1)
    out = format_tasks(tasks)
    assert "[x] 1. a" in out
    assert "[ ] 2. b" in out
