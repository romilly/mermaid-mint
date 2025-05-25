# Next Session Instructions

## Context
This is a new project created to convert YAML process definitions to Mermaid flowcharts instead of BPMN. The previous py-bpmn project showed that Mermaid has better auto-layout capabilities and all needed features.

## What's Been Done
1. ✅ Project structure created with TDD setup
2. ✅ Name validation (GitHub/PyPI compliant: `mermaid-mint`)
3. ✅ Standard Python project layout with src/mermaid_mint/
4. ✅ Test framework configured (pytest)
5. ✅ CLAUDE.md with TDD workflow documented

## Immediate Next Steps

### 1. Initialize Development Environment
```bash
cd /home/romilly/git/active/mermaid-mint
python -m venv venv
source venv/bin/activate
pip install -e .[test]
```

### 2. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial project structure"
```

### 3. Start TDD Development
**Goal**: Convert YAML process definitions to Mermaid flowchart syntax

**First Feature**: Simple linear process (start → task → end)
- Write failing test for YAML→Mermaid conversion
- Implement minimal parser and converter
- Follow Red-Green-Refactor-Commit cycle

### 4. Reference Examples
Use the same YAML schema from py-bpmn:
```yaml
process:
  id: example
  name: Example Process  
  steps:
    - type: start
      id: start
      next: task1
    - type: task
      id: task1
      name: Do Something
      next: end
    - type: end
      id: end
```

Target Mermaid output:
```mermaid
flowchart TD
    start([Start]) --> task1[Do Something]
    task1 --> end([End])
```

### 5. Key Advantages of Mermaid
- Better automatic layout than BPMN
- Simpler syntax
- Built-in GitHub/GitLab rendering
- No manual positioning needed

## Session Commands
1. **Open new Claude Code session in mermaid-mint directory**
2. **Follow TDD workflow from CLAUDE.md**
3. **Start with simplest possible test case**

## Dependencies to Add
Consider adding:
- `PyYAML` for YAML parsing
- `pathlib` for file handling
- Standard library only initially (keep it simple)

Delete this file once development starts.