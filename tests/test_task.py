"""Tests for Task class - process task/activity."""

import pytest
from mermaid_mint.steps import Task


def test_task_creation():
    """Test creating a Task step with step_id and name."""
    task = Task("t1", "Process Data")
    
    assert task.step_id == "t1"
    assert task.name == "Process Data"
    assert task.successor is None