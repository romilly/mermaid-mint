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
        step_formatters = {
            Start: self._format_start_step,
            Task: self._format_task_step,
            Decision: self._format_decision_step,
            End: self._format_end_step
        }
        
        step_type = type(step)
        if step_type in step_formatters:
            lines.append(step_formatters[step_type](step))
        
        # Add connections
        self._add_connections(step, lines, visited)
    
    def _format_start_step(self, step):
        """Format a Start step for Mermaid."""
        return f"    {step.step_id}[{step.name}]"
    
    def _format_task_step(self, step):
        """Format a Task step for Mermaid."""
        return f"    {step.step_id}[{step.name}]"
    
    def _format_decision_step(self, step):
        """Format a Decision step for Mermaid."""
        return f"    {step.step_id}{{{step.name}}}"
    
    def _format_end_step(self, step):
        """Format an End step for Mermaid."""
        return f"    {step.step_id}[{step.name}]"
    
    def _add_connections(self, step, lines, visited):
        """Add connections for a step and recursively process connected steps."""
        if hasattr(step, 'successor') and step.successor:
            lines.append(f"    {step.step_id} --> {step.successor.step_id}")
            self._collect_steps(step.successor, lines, visited)
        
        if hasattr(step, 'yes') and step.yes:
            lines.append(f"    {step.step_id} --> {step.yes.step_id}")
            self._collect_steps(step.yes, lines, visited)
        
        if hasattr(step, 'no') and step.no:
            lines.append(f"    {step.step_id} --> {step.no.step_id}")
            self._collect_steps(step.no, lines, visited)