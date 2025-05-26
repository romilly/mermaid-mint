"""Tests for MermaidVisitor - generating Mermaid diagrams from Process objects."""

import pytest
from mermaid_mint.visitors import MermaidVisitor
from mermaid_mint.parser import Parser
from tests.helpers.sample_data import PROCESS, PROCESS_WITH_RESOURCES


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


def test_mermaid_visitor_generates_diagram_with_resources():
    """Test that MermaidVisitor generates diagram with Database, Document, and operations."""
    parser = Parser()
    process = parser.parse_string(PROCESS_WITH_RESOURCES)
    
    visitor = MermaidVisitor()
    mermaid_output = visitor.visit_process(process)
    
    # Basic structure
    assert isinstance(mermaid_output, str)
    assert "flowchart TD" in mermaid_output
    
    # Check Database resources are rendered
    assert "orders_db[(Orders Database)]" in mermaid_output
    assert "inventory_db[(Inventory Database)]" in mermaid_output
    assert "payment_db[(Payment Database)]" in mermaid_output
    
    # Check Document resources are rendered
    assert "audit_log[/Audit Log/]" in mermaid_output
    assert "notification_doc[/Customer Notification/]" in mermaid_output
    
    # Check Task with operations shows connections to resources
    assert "save_order --> orders_db" in mermaid_output
    assert "save_order --> audit_log" in mermaid_output
    assert "process_payment --> payment_db" in mermaid_output
    assert "backorder --> orders_db" in mermaid_output
    assert "backorder --> notification_doc" in mermaid_output
    
    # Check Decision with Query test shows connection to resource
    assert "check_inventory --> inventory_db" in mermaid_output
    
    # Check regular step connections still work
    assert "start --> save_order" in mermaid_output
    assert "save_order --> check_inventory" in mermaid_output