"""Tests for Parser class - YAML to Process object conversion."""

import pytest
from mermaid_mint.parser import Parser
from mermaid_mint.steps import Process, Start, Task, Decision, End, Database, Document, Query, Update
from tests.helpers.sample_data import PROCESS, PROCESS_WITH_RESOURCES


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


def test_parser_creates_process_with_resources_and_operations():
    """Test that Parser creates process with Database, Document, and operations."""
    parser = Parser()
    process = parser.parse_string(PROCESS_WITH_RESOURCES)
    
    # Check process basics
    assert process.process_id == "order_processing"
    assert process.name == "Order Processing Workflow"
    
    # Check that resources are created correctly
    orders_db = process["orders_db"]
    assert isinstance(orders_db, Database)
    assert orders_db.name == "Orders Database"
    
    audit_log = process["audit_log"]
    assert isinstance(audit_log, Document)
    assert audit_log.name == "Audit Log"
    
    # Check task with operations
    save_order = process["save_order"]
    assert isinstance(save_order, Task)
    assert len(save_order.operations) == 2
    
    # Check first operation
    op1 = save_order.operations[0]
    assert isinstance(op1, Update)
    assert op1.target == orders_db
    assert op1.description == "Insert new order record"
    
    # Check second operation
    op2 = save_order.operations[1]
    assert isinstance(op2, Update)
    assert op2.target == audit_log
    assert op2.description == "Log order creation event"
    
    # Check decision with query test
    check_inventory = process["check_inventory"]
    assert isinstance(check_inventory, Decision)
    assert isinstance(check_inventory.test, Query)
    assert check_inventory.test.target == process["inventory_db"]
    assert check_inventory.test.description == "Check if product is in stock"