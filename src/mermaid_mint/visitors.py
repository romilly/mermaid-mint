"""Visitor classes for generating different output formats from Process objects."""

from .steps import Process, Start, Task, Decision, End


class MermaidVisitor:
    """Visitor that generates Mermaid flowchart syntax from Process objects."""
    
    def visit_process(self, process: Process) -> str:
        """Generate Mermaid diagram from a Process."""
        lines = ["flowchart TD"]
        
        # Add all step definitions
        for step_id in process.step_ids():
            step = process[step_id]
            lines.append(self._format_step(step))
        
        # Add all connections
        for step_id in process.step_ids():
            step = process[step_id]
            lines.extend(self._get_connections(step))
        
        return "\n".join(lines)
    
    def _format_step(self, step):
        """Format a step for Mermaid output."""
        step_formatters = {
            Start: self._format_start_step,
            Task: self._format_task_step,
            Decision: self._format_decision_step,
            End: self._format_end_step
        }
        
        step_type = type(step)
        if step_type in step_formatters:
            return step_formatters[step_type](step)
        return ""
    
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
    
    def _get_connections(self, step):
        """Get all connections for a step."""
        connections = []
        
        if hasattr(step, 'successor') and step.successor:
            connections.append(f"    {step.step_id} --> {step.successor.step_id}")
        
        if hasattr(step, 'yes') and step.yes:
            connections.append(f"    {step.step_id} --> {step.yes.step_id}")
        
        if hasattr(step, 'no') and step.no:
            connections.append(f"    {step.step_id} --> {step.no.step_id}")
        
        return connections