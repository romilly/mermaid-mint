"""Parser for converting YAML to Process objects."""

import yaml
from .steps import Process, Start, Task, Decision, End


class Parser:
    """Parses YAML files to create Process objects."""
    
    def parse_file(self, file_path: str) -> Process:
        """Parse a YAML file and return a Process object."""
        with open(file_path, 'r') as process_file:
            return self.parse_string(process_file.read())

    def parse_string(self, raw_data):
        data = yaml.safe_load(raw_data)
        process_data = data['process']
        # Create all steps
        steps = {}
        for step_data in data['steps']:
            step = self._create_step(step_data)
            steps[step.step_id] = step
        # Connect steps
        self._connect_steps(data['steps'], steps)
        # Find the start step
        start_step = next(step for step in steps.values() if isinstance(step, Start))
        process = Process(
            process_id=process_data['process_id'],
            name=process_data['name'],
            start=start_step
        )
        return process

    def _create_step(self, step_data):
        """Create a step object from step data."""
        step_type = step_data['type']
        step_id = step_data['step_id']
        name = step_data['name']
        
        if step_type == 'Start':
            return Start(step_id, name)
        elif step_type == 'Task':
            return Task(step_id, name)
        elif step_type == 'Decision':
            return Decision(step_id, name, step_data.get('test', ''))
        elif step_type == 'End':
            return End(step_id, name)
        else:
            raise ValueError(f"Unknown step type: {step_type}")
    
    def _connect_steps(self, steps_data, steps):
        """Connect steps based on successor/yes/no references."""
        for step_data in steps_data:
            step = steps[step_data['step_id']]
            
            if hasattr(step, 'successor') and 'successor' in step_data:
                step.successor = steps[step_data['successor']]
            
            if hasattr(step, 'yes') and 'yes' in step_data:
                step.yes = steps[step_data['yes']]
            
            if hasattr(step, 'no') and 'no' in step_data:
                step.no = steps[step_data['no']]