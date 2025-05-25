# ADR-0002: Use Dataclasses for Step Objects

## Status

Accepted

## Context

The process DSL requires step objects (Start, End, Task, Decision) that hold data and have simple behavior. These objects need clear initialization, readable attribute access, and automatic generation of common methods like `__repr__` and `__eq__`.

## Decision

Use Python dataclasses for all step objects instead of traditional classes with manual `__init__` methods. This includes the base Step class and all derived classes (Start, End, Task, Decision).

## Consequences

### Positive
- Cleaner, more readable code with less boilerplate
- Automatic generation of `__init__`, `__repr__`, `__eq__` methods
- Clear declaration of object attributes at class level
- Better IDE support and type hints
- Consistent object behavior across all step types