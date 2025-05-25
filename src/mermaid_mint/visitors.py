"""Visitor classes for generating different output formats from Process objects."""

from .steps import Process, Start, Task, Decision, End


class MermaidVisitor:
    """Visitor that generates Mermaid flowchart syntax from Process objects."""
    
    def visit_process(self, process: Process) -> str:
        """Generate Mermaid diagram from a Process."""
        lines = ["flowchart TD"]
        
        # Collect all steps by traversing from start
        visited = set()
        self._collect_steps(process.start, lines, visited)
        
        return "\n".join(lines)
    
    def _collect_steps(self, step, lines, visited):
        """Recursively collect steps and their connections."""
        if not step or step.step_id in visited:
            return
        
        visited.add(step.step_id)
        
        # Add step definition
        if isinstance(step, Start):
            lines.append(f"    {step.step_id}[{step.name}]")
        elif isinstance(step, Task):
            lines.append(f"    {step.step_id}[{step.name}]")
        elif isinstance(step, Decision):
            lines.append(f"    {step.step_id}{{{step.name}}}")
        elif isinstance(step, End):
            lines.append(f"    {step.step_id}[{step.name}]")
        
        # Add connections
        if hasattr(step, 'successor') and step.successor:
            lines.append(f"    {step.step_id} --> {step.successor.step_id}")
            self._collect_steps(step.successor, lines, visited)
        
        if hasattr(step, 'yes') and step.yes:
            lines.append(f"    {step.step_id} --> {step.yes.step_id}")
            self._collect_steps(step.yes, lines, visited)
        
        if hasattr(step, 'no') and step.no:
            lines.append(f"    {step.step_id} --> {step.no.step_id}")
            self._collect_steps(step.no, lines, visited)