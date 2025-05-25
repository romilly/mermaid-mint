"""Tests for Parser class - YAML to Process object conversion."""

import pytest
from mermaid_mint.parser import Parser
from mermaid_mint.steps import Process, Start


def test_parser_reads_yaml_and_creates_process():
    """Test that Parser can read YAML file and create Process object."""
    parser = Parser()
    process = parser.parse_file("tests/data/sample_process.yaml")
    
    assert isinstance(process, Process)
    assert process.process_id == "user_registration"
    assert process.name == "User Registration Process"
    assert process.start is not None


def test_parser_creates_start_from_yaml():
    """Test that Parser creates start step from YAML file data."""
    parser = Parser()
    process = parser.parse_file("tests/data/sample_process.yaml")
    
    assert isinstance(process.start, Start)
    assert process.start.step_id == "start"
    assert process.start.name == "Begin Registration"