"""Process step classes for the mermaid-mint DSL."""

from dataclasses import dataclass


@dataclass
class Step:
    """Base class for all process steps."""
    step_id: str
    name: str


@dataclass
class TerminalStep(Step):
    """Base class for steps with no successor."""
    pass


@dataclass
class NonTerminalStep(Step):
    """Base class for steps with successor(s)."""
    successor: Step = None


@dataclass
class Start(NonTerminalStep):
    """Starting point of a process."""
    pass


@dataclass
class End(TerminalStep):
    """End point of a process."""
    pass


@dataclass
class Task(NonTerminalStep):
    """A task/activity in the process."""
    pass


@dataclass
class Decision(Step):
    """A decision point with yes/no branches."""
    test: str = ""
    yes: Step = None
    no: Step = None


@dataclass
class Process:
    """Complete process workflow."""
    process_id: str
    name: str
    start: Step = None
    
    def __post_init__(self):
        """Initialize the steps dictionary after dataclass init."""
        self._steps = {}
    
    def add_step(self, step: Step):
        """Add a step to the process."""
        self._steps[step.step_id] = step
    
    def step_ids(self):
        """Return a list of all step IDs in the process."""
        return list(self._steps.keys())
    
    def get_step(self, step_id: str):
        """Return the step with the given ID, or None if not found."""
        return self._steps.get(step_id)
    
    def __getitem__(self, step_id: str):
        """Get a step by ID using indexing syntax."""
        return self._steps[step_id]
    
    def __setitem__(self, step_id: str, step: Step):
        """Set a step by ID using indexing syntax."""
        self._steps[step_id] = step