"""Tests for End class - process end point."""

import pytest
from mermaid_mint.steps import End


def test_end_creation():
    """Test creating an End step with step_id and name."""
    end = End("e1", "Process Complete")
    
    assert end.step_id == "e1"
    assert end.name == "Process Complete"