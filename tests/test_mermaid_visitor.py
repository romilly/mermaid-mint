"""Tests for MermaidVisitor - generating Mermaid diagrams from Process objects."""

import pytest
from mermaid_mint.visitors import MermaidVisitor
from mermaid_mint.parser import Parser
from tests.helpers.sample_data import PROCESS


def test_mermaid_visitor_generates_diagram():
    """Test that MermaidVisitor generates a Mermaid diagram from a Process."""
    parser = Parser()
    process = parser.parse_string(PROCESS)
    
    visitor = MermaidVisitor()
    mermaid_output = visitor.visit_process(process)
    
    assert isinstance(mermaid_output, str)
    assert "flowchart TD" in mermaid_output
    assert "start[Begin Registration]" in mermaid_output
    assert "validate_email[Validate Email Address]" in mermaid_output
    assert "check_existing_user{Check if User Exists}" in mermaid_output
    assert "start --> validate_email" in mermaid_output