"""Tests for Process class - complete process workflow."""

import pytest
from mermaid_mint.steps import Process, Start, Task, End


def test_process_creation():
    """Test creating a Process with process_id and name."""
    process = Process("p1", "User Registration")
    
    assert process.process_id == "p1"
    assert process.name == "User Registration"
    assert process.start is None


def test_process_with_start():
    """Test Process with start step."""
    process = Process("p1", "User Registration")
    start = Start("s1", "Begin")
    
    process.start = start
    
    assert process.start is start


def test_process_step_ids():
    """Test that Process can list all step IDs."""
    process = Process("p1", "Test Process")
    start = Start("s1", "Begin")
    task = Task("t1", "Task")
    end = End("e1", "End")
    
    process.add_step(start)
    process.add_step(task)
    process.add_step(end)
    
    step_ids = process.step_ids()
    assert set(step_ids) == {"s1", "t1", "e1"}


def test_process_get_step():
    """Test that Process can return a step by ID."""
    process = Process("p1", "Test Process")
    start = Start("s1", "Begin")
    task = Task("t1", "Task")
    
    process.add_step(start)
    process.add_step(task)
    
    assert process.get_step("s1") is start
    assert process.get_step("t1") is task
    assert process.get_step("nonexistent") is None