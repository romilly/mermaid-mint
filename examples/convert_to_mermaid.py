#!/usr/bin/env python3
"""Convert YAML process definitions to Mermaid diagrams."""

import sys
from pathlib import Path

from mermaid_mint.parser import Parser
from mermaid_mint.visitors import MermaidVisitor


def yaml_to_mermaid(yaml_file_path: str, output_file_path: str = None) -> str:
    """
    Convert a YAML process definition to a Mermaid diagram.
    
    Args:
        yaml_file_path: Path to the YAML file to convert
        output_file_path: Optional path for output .mmd file. If not provided,
                         uses the same name as input file with .mmd extension
    
    Returns:
        The generated Mermaid diagram as a string
    """
    # Parse the YAML file
    parser = Parser()
    process = parser.parse_file(yaml_file_path)
    
    # Generate Mermaid diagram
    visitor = MermaidVisitor()
    mermaid_diagram = visitor.visit_process(process)
    
    # Determine output file path
    if output_file_path is None:
        yaml_path = Path(yaml_file_path)
        output_file_path = yaml_path.with_suffix('.mmd')
    
    # Write to file
    with open(output_file_path, 'w') as f:
        f.write(mermaid_diagram)
    
    print(f"Converted {yaml_file_path} to {output_file_path}")
    return mermaid_diagram


def main():
    """Command line interface for the converter."""
    if len(sys.argv) < 2:
        print("Usage: python convert_to_mermaid.py <yaml_file> [output_file]")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        yaml_to_mermaid(yaml_file, output_file)
    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()