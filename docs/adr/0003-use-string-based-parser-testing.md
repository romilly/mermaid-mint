# ADR-0003: Use String-Based Parser Testing

## Status

Accepted

## Context

Initial parser tests used file-based YAML input, but this created issues:
1. File paths were not correct when debugging tests in PyCharm
2. YAML parser converted unquoted `yes`/`no` to boolean `True`/`False`
3. Tests were harder to debug and maintain

## Decision

Use string-based YAML input for parser tests instead of file-based input. Store test YAML data as string constants in a helper module and use a `parse_string()` method alongside the existing `parse_file()` method.

## Consequences

### Positive
- Tests can be debugged properly in PyCharm
- Test data is inline and easily readable
- Better control over YAML content (can quote special values)
- Faster test execution (no file I/O)
- Test data is version controlled with the test code

### Neutral
- Still maintain `parse_file()` for production use