"""Process step classes for the mermaid-mint DSL."""

from dataclasses import dataclass


@dataclass
class Step:
    """Base class for all process steps."""
    step_id: str
    name: str


class Start(Step):
    """Starting point of a process."""
    
    def __init__(self, step_id: str, name: str):
        super().__init__(step_id, name)
        self.successor = None
    
    def set_successor(self, step: Step):
        """Set the next step in the process."""
        self.successor = step


class Task(Step):
    """A task/activity in the process."""
    
    def __init__(self, step_id: str, name: str):
        super().__init__(step_id, name)
        self.successor = None
    
    def set_successor(self, step: Step):
        """Set the next step in the process."""
        self.successor = step