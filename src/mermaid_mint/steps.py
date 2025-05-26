"""Process step classes for the mermaid-mint DSL."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Union, List


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
class Resource(TerminalStep):
    """Base class for resources that can be updated or queried."""
    pass


@dataclass
class Database(Resource):
    """A database that can be updated or queried."""
    pass


@dataclass
class Document(Resource):
    """A document that can be updated or queried."""
    pass


@dataclass
class Operation(ABC):
    """Abstract base class for operations on resources."""
    target: Resource
    description: str


@dataclass
class Query(Operation):
    """Query operation on a resource."""
    pass


@dataclass
class Update(Operation):
    """Update operation on a resource."""
    pass


@dataclass
class Task(NonTerminalStep):
    """A task/activity in the process."""
    operations: List[Operation] = field(default_factory=list)


@dataclass
class Decision(Step):
    """A decision point with yes/no branches."""
    test: Union[str, Query] = ""
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