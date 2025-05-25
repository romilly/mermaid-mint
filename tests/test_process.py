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