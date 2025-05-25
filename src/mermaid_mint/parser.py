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
        
        step_creators = {
            'Start': self._create_start_step,
            'Task': self._create_task_step,
            'Decision': self._create_decision_step,
            'End': self._create_end_step
        }
        
        if step_type not in step_creators:
            raise ValueError(f"Unknown step type: {step_type}")
        
        return step_creators[step_type](step_data)
    
    def _create_start_step(self, step_data):
        """Create a Start step from step data."""
        return Start(step_data['step_id'], step_data['name'])
    
    def _create_task_step(self, step_data):
        """Create a Task step from step data."""
        return Task(step_data['step_id'], step_data['name'])
    
    def _create_decision_step(self, step_data):
        """Create a Decision step from step data."""
        return Decision(step_data['step_id'], step_data['name'], step_data.get('test', ''))
    
    def _create_end_step(self, step_data):
        """Create an End step from step data."""
        return End(step_data['step_id'], step_data['name'])
    
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