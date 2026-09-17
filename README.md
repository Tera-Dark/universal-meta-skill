# Universal Meta-Skill

A host-aware meta-skill for creating, refactoring, auditing, evolving, repairing, migrating, and packaging agent skills.

## Design goals

- Portable core with host-specific extensions separated.
- Contract-first workflow.
- Evidence-based verification.
- Progressive disclosure.
- Explicit scope and authority boundaries.
- Fast path for simple tasks.
- Lifecycle and migration support.

## Directory layout

```text
SKILL.md
README.md
CHANGELOG.md
references/
  evaluation-protocol.md
  host-capability-matrix.md
  metadata-profiles.md
  minimal-skill-template.md
scripts/
tests/
  fixtures/
```

The reference files are deliberately separated from the root skill so the core remains readable and easier to load.
