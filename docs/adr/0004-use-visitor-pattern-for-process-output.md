# ADR-0004: Use Visitor Pattern for Process Output

## Status

Accepted

## Context

We need to generate different output formats from Process objects, starting with Mermaid diagram definitions. Future requirements may include other formats like PlantUML, DOT/Graphviz, or custom formats. The output generation logic should be extensible without modifying the core step classes.

## Decision

Use the Visitor pattern to generate output from Process objects. Create a base `Visitor` class and specific implementations like `MermaidVisitor`. Steps will accept visitors, allowing different output formats to be generated without coupling output logic to the step classes.

## Consequences

### Positive
- Clean separation of concerns (step logic vs output formatting)
- Easy to add new output formats without modifying existing step classes
- Follows Open/Closed Principle (open for extension, closed for modification)
- Testable output generation logic in isolation
- Consistent pattern for all output formats

### Neutral
- Requires understanding of Visitor pattern for maintainers