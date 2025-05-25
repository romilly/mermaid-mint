"""Tests for Decision class - process decision point."""

import pytest
from mermaid_mint.steps import Decision, Task, End


def test_decision_creation():
    """Test creating a Decision step with step_id, name, and test."""
    decision = Decision("d1", "Check Status", "status == 'ready'")
    
    assert decision.step_id == "d1"
    assert decision.name == "Check Status"
    assert decision.test == "status == 'ready'"
    assert decision.yes is None
    assert decision.no is None


def test_decision_with_successors():
    """Test Decision with yes and no successors."""
    decision = Decision("d1", "Check Status", "status == 'ready'")
    yes_task = Task("t1", "Process")
    no_end = End("e1", "Skip")
    
    decision.yes = yes_task
    decision.no = no_end
    
    assert decision.yes is yes_task
    assert decision.no is no_end