"""Process step classes for the mermaid-mint DSL."""


class Step:
    """Base class for all process steps."""
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Start(Step):
    """Starting point of a process."""
    
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.successor = None
    
    def set_successor(self, step: Step):
        """Set the next step in the process."""
        self.successor = step


class Task(Step):
    """A task/activity in the process."""
    
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.successor = None
    
    def set_successor(self, step: Step):
        """Set the next step in the process."""
        self.successor = step