"""Tests for Start class - process starting point."""

import pytest
from mermaid_mint.steps import Start, Task


def test_start_creation():
    """Test creating a Start step with id and name."""
    start = Start("s1", "Begin Process")
    
    assert start.id == "s1"
    assert start.name == "Begin Process"
    assert start.successor is None


def test_start_set_successor():
    """Test setting successor for Start step."""
    start = Start("s1", "Begin Process")
    task = Task("t1", "First Task")
    
    start.set_successor(task)
    
    assert start.successor is task