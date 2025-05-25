"""Process step classes for the mermaid-mint DSL."""

from dataclasses import dataclass


@dataclass
class Step:
    """Base class for all process steps."""
    step_id: str
    name: str


@dataclass
class Start(Step):
    """Starting point of a process."""
    successor: Step = None


@dataclass
class End(Step):
    """End point of a process."""
    pass


@dataclass
class Task(Step):
    """A task/activity in the process."""
    successor: Step = None