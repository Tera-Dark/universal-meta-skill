# Universal Meta Skill

**English** | [简体中文](README.md)

A host-aware meta-skill for creating, refactoring, auditing, evolving, repairing, migrating, testing, and packaging Agent Skills.

## Design goals

- Compatible core `SKILL.md`
- Conditional rather than universal prompt-engineering mechanisms
- Explicit scope, authority, and tool boundaries
- Progressive disclosure through optional resources
- Behavior validation and regression testing
- Honest `UNKNOWN` / `NOT EXECUTED` reporting

## Layout

```text
universal-meta-skill/
├── .gitignore
├── CHANGELOG.md               # Version history
├── README.md                  # [Default] Chinese documentation
├── README_EN.md               # English documentation
├── SKILL.md                   # [Default Entry] Chinese core specification
├── SKILL_EN.md                # English core specification
├── scripts/                   # Automated validation scripts (zero dependencies)
│   └── validate_skill.py      # Static compliance and reference checker
├── tests/                     # Test fixtures and test documentation
│   ├── fixtures/
│   │   ├── ambiguous-request.md
│   │   ├── missing-input.md
│   │   └── out-of-scope.md
│   └── README.md
└── references/                # References & templates (Chinese)
    ├── minimal-skill-template.md
    ├── evaluation-protocol.md
    ├── host-capability-matrix.md
    ├── metadata-profiles.md
    └── en/                    # Complete English references mirror
        ├── minimal-skill-template.md
        ├── evaluation-protocol.md
        ├── host-capability-matrix.md
        └── metadata-profiles.md
```

## Quick Start

### 1. Load into an Agent Host
Place this repository directory into the skill search path defined by your target host (e.g. Antigravity, Claude Code, OpenCode), and verify discovery, loading, and runtime execution according to that host's documentation. Different hosts may require additional configuration.

### 2. Automated Static Validation
Run the built-in zero-dependency verification script to validate frontmatter and check reference integrity:

```bash
python scripts/validate_skill.py
```
