# mermaid-mint

A Python DSL for creating process diagrams that can be converted to Mermaid flowcharts.

## Overview

Mermaid-mint allows you to define business processes using a simple YAML syntax and convert them to Mermaid diagram format. The project follows strict TDD principles and uses clean architectural patterns.

## Features

- **Process Definition**: Define processes with Start, Task, Decision, and End steps
- **YAML Input**: Human-readable YAML format for process definitions
- **Mermaid Output**: Generate Mermaid flowchart syntax from process definitions
- **Extensible Architecture**: Dictionary dispatch patterns and visitor pattern for easy extension

## Quick Start

### Define a Process in YAML

```yaml
process:
  process_id: "user_registration"
  name: "User Registration Process"
  
steps:
  - step_id: "start"
    type: "Start"
    name: "Begin Registration"
    successor: "validate_email"
    
  - step_id: "validate_email"
    type: "Task"
    name: "Validate Email Address"
    successor: "check_existing_user"
    
  - step_id: "check_existing_user"
    type: "Decision"
    name: "Check if User Exists"
    test: "user_exists == true"
    "yes": "reject_duplicate"
    "no": "create_account"
    
  - step_id: "reject_duplicate"
    type: "Task"
    name: "Reject Duplicate User"
    successor: "end_rejected"
    
  - step_id: "create_account"
    type: "Task"
    name: "Create User Account"
    successor: "end_success"
    
  - step_id: "end_rejected"
    type: "End"
    name: "Registration Rejected"
    
  - step_id: "end_success"
    type: "End"
    name: "Registration Complete"
```

### Convert to Mermaid

```python
from mermaid_mint.parser import Parser
from mermaid_mint.visitors import MermaidVisitor

# Parse YAML
parser = Parser()
process = parser.parse_file("process.yaml")

# Generate Mermaid diagram
visitor = MermaidVisitor()
mermaid_output = visitor.visit_process(process)
print(mermaid_output)
```

## Architecture

### Key Design Decisions

See `docs/adr/` for detailed architectural decision records:

- **ADR-0002**: Use dataclasses for step objects
- **ADR-0003**: String-based parser testing for better debugging
- **ADR-0004**: Visitor pattern for extensible output formats

### Core Components

- **`mermaid_mint.steps`**: Process and step dataclasses (Start, Task, Decision, End)
- **`mermaid_mint.parser`**: YAML to Process object conversion
- **`mermaid_mint.visitors`**: Output format generators (currently Mermaid)

### Design Patterns

- **Dictionary Dispatch**: Used in Parser and MermaidVisitor for extensibility
- **Visitor Pattern**: For generating different output formats
- **Pythonic Indexing**: Process objects support `process[step_id]` syntax

## Development

### Setup

```bash
# Activate virtual environment
source venv/bin/activate

# Install in development mode
pip install -e .[test]
```

### Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_parser.py -v
```

### Project follows strict TDD

See `CLAUDE.md` for detailed TDD workflow and guidelines.

## Current Status

✅ **Complete**: Basic DSL with all step types  
✅ **Complete**: YAML parsing with proper boolean handling  
✅ **Complete**: Mermaid output generation  
✅ **Complete**: Comprehensive test coverage (13 tests)  
✅ **Complete**: Clean architecture with established patterns  

## Installation

```bash
pip install -e .
```
