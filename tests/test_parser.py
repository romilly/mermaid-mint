"""Tests for Parser class - YAML to Process object conversion."""

import pytest
from mermaid_mint.parser import Parser
from mermaid_mint.steps import Process, Start, Task, Decision, End
from tests.helpers.sample_data import PROCESS


def test_parser_creates_complete_process():
    """Test that Parser creates complete process with all steps and connections."""
    parser = Parser()
    process = parser.parse_string(PROCESS)
    
    # Check start step and its successor
    start = process.start
    assert start.step_id == "start"
    assert isinstance(start.successor, Task)
    assert start.successor.step_id == "validate_email"
    
    # Check task step and its successor
    validate_email = start.successor
    assert validate_email.name == "Validate Email Address"
    assert isinstance(validate_email.successor, Decision)
    assert validate_email.successor.step_id == "check_existing_user"
    
    # Check decision step and its branches
    decision = validate_email.successor
    assert decision.name == "Check if User Exists"
    assert decision.test == "user_exists == true"
    assert isinstance(decision.yes, Task)
    assert decision.yes.step_id == "reject_duplicate"
    assert isinstance(decision.no, Task)
    assert decision.no.step_id == "create_account"
    
    # Check reject path
    reject_task = decision.yes
    assert reject_task.name == "Reject Duplicate User"
    assert isinstance(reject_task.successor, End)
    assert reject_task.successor.step_id == "end_rejected"
    
    # Check create account path
    create_account = decision.no
    assert create_account.name == "Create User Account"
    assert isinstance(create_account.successor, Task)
    assert create_account.successor.step_id == "send_confirmation"
    
    # Check confirmation task
    send_confirmation = create_account.successor
    assert send_confirmation.name == "Send Confirmation Email"
    assert isinstance(send_confirmation.successor, End)
    assert send_confirmation.successor.step_id == "end_success"