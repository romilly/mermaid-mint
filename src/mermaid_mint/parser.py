"""Parser for converting YAML to Process objects."""

import yaml
from .steps import Process, Start, Task, Decision, End, Database, Document, Query, Update


class Parser:
    """Parses YAML files to create Process objects."""
    
    def parse_file(self, file_path: str) -> Process:
        """Parse a YAML file and return a Process object."""
        with open(file_path, 'r') as process_file:
            return self.parse_string(process_file.read())

    def parse_string(self, raw_data):
        data = yaml.safe_load(raw_data)
        process_data = data['process']
        # Create process
        process = Process(
            process_id=process_data['process_id'],
            name=process_data['name']
        )
        
        # Create all steps and add to process
        for step_data in data['steps']:
            step = self._create_step(step_data)
            process[step.step_id] = step
        
        # Connect steps
        self._connect_steps(data['steps'], process)
        
        # Connect operations (resolve target references)
        self._connect_operations(data['steps'], process)
        
        # Find and set the start step
        start_step = next(step for step in process.step_ids() if isinstance(process[step], Start))
        process.start = process[start_step]
        return process

    def _create_step(self, step_data):
        """Create a step object from step data."""
        step_type = step_data['type']
        
        step_creators = {
            'Start': self._create_start_step,
            'Task': self._create_task_step,
            'Decision': self._create_decision_step,
            'End': self._create_end_step,
            'Database': self._create_database_step,
            'Document': self._create_document_step
        }
        
        if step_type not in step_creators:
            raise ValueError(f"Unknown step type: {step_type}")
        
        return step_creators[step_type](step_data)
    
    def _create_start_step(self, step_data):
        """Create a Start step from step data."""
        return Start(step_data['step_id'], step_data['name'])
    
    def _create_task_step(self, step_data):
        """Create a Task step from step data."""
        task = Task(step_data['step_id'], step_data['name'])
        
        # Parse operations if present
        if 'operations' in step_data:
            for op_data in step_data['operations']:
                operation = self._create_operation(op_data)
                task.operations.append(operation)
        
        return task
    
    def _create_decision_step(self, step_data):
        """Create a Decision step from step data."""
        test_data = step_data.get('test', '')
        
        # Check if test is a Query object or a string
        if isinstance(test_data, dict) and test_data.get('type') == 'Query':
            test = self._create_operation(test_data)
        else:
            test = test_data
            
        return Decision(step_data['step_id'], step_data['name'], test)
    
    def _create_end_step(self, step_data):
        """Create an End step from step data."""
        return End(step_data['step_id'], step_data['name'])
    
    def _create_database_step(self, step_data):
        """Create a Database step from step data."""
        return Database(step_data['step_id'], step_data['name'])
    
    def _create_document_step(self, step_data):
        """Create a Document step from step data."""
        return Document(step_data['step_id'], step_data['name'])
    
    def _create_operation(self, op_data):
        """Create an Operation object from operation data."""
        op_type = op_data['type']
        
        # Note: target will be resolved in _connect_operations
        if op_type == 'Query':
            return Query(target=op_data['target'], description=op_data['description'])
        elif op_type == 'Update':
            return Update(target=op_data['target'], description=op_data['description'])
        else:
            raise ValueError(f"Unknown operation type: {op_type}")
    
    def _connect_steps(self, steps_data, process):
        """Connect steps based on successor/yes/no references."""
        for step_data in steps_data:
            step = process[step_data['step_id']]
            
            if hasattr(step, 'successor') and 'successor' in step_data:
                step.successor = process[step_data['successor']]
            
            if hasattr(step, 'yes') and 'yes' in step_data:
                step.yes = process[step_data['yes']]
            
            if hasattr(step, 'no') and 'no' in step_data:
                step.no = process[step_data['no']]
    
    def _connect_operations(self, steps_data, process):
        """Connect operation targets to actual Resource objects."""
        for step_data in steps_data:
            step = process[step_data['step_id']]
            
            # Handle Task operations
            if hasattr(step, 'operations') and 'operations' in step_data:
                for i, op_data in enumerate(step_data['operations']):
                    target_id = op_data['target']
                    step.operations[i].target = process[target_id]
            
            # Handle Decision test if it's a Query
            if hasattr(step, 'test') and isinstance(step.test, Query):
                # Find the test data to get the target reference
                test_data = step_data.get('test', {})
                if isinstance(test_data, dict) and 'target' in test_data:
                    target_id = test_data['target']
                    step.test.target = process[target_id]