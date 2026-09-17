# Tests & Evaluation Fixtures

This directory contains evaluation fixtures corresponding to the **Evaluation Protocol (Level 2 & Level 3)** defined in `references/evaluation-protocol.md`.

## Fixtures Overview

- `fixtures/ambiguous-request.md`: Evaluates handling of vague user prompts and contract clarification.
- `fixtures/missing-input.md`: Evaluates missing prerequisite detection and safe defaults.
- `fixtures/out-of-scope.md`: Evaluates authority boundaries, security rules, and injection resistance.

## Running Tests

1. Feed the input scenario to an agent equipped with this Meta-Skill.
2. Compare the agent's response against the Evaluation Criteria in the fixture.
3. Record the result using the format:
```text
Status: PASS | FAIL | PARTIAL | UNKNOWN
Evidence: [Observed behavior]
Limitations: [Unverified assumptions]
```
