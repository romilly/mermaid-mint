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
        process = Process(
            process_id=process_data['process_id'],
            name=process_data['name'],
            start=Start("dummy", "dummy")
        )
        
        return process