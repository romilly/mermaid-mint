"""Parser for converting YAML to Process objects."""

import yaml
from .steps import Process, Start


class Parser:
    """Parses YAML files to create Process objects."""
    
    def parse_file(self, file_path: str) -> Process:
        """Parse a YAML file and return a Process object."""
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        
        process_data = data['process']
        
        # Find the start step
        start_step_data = next(step for step in data['steps'] if step['type'] == 'Start')
        start_step = Start(start_step_data['step_id'], start_step_data['name'])
        
        process = Process(
            process_id=process_data['process_id'],
            name=process_data['name'],
            start=start_step
        )
        
        return process