# Universal Meta Skill

**English** | [简体中文](README.md)

A host-aware meta-skill for creating, refactoring, auditing, evolving, repairing, migrating, testing, and packaging Agent Skills.

## Design goals

- Compatible core SKILL.md
- Conditional rather than universal prompt-engineering mechanisms
- Explicit scope, authority, and tool boundaries
- Progressive disclosure through optional resources
- Behavior validation and regression testing
- Honest UNKNOWN / NOT EXECUTED reporting

## Layout

`	ext
universal-meta-skill/
├── .gitignore
├── CHANGELOG.md               # Version history
├── README.md                  # [Default] Chinese documentation
├── README_EN.md               # English documentation
├── SKILL.md                   # [Default Entry] Chinese core specification
├── SKILL_EN.md                # English core specification
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
`

This repository provides both Chinese and English versions. Root SKILL.md defaults to Chinese for domestic agent alignment, while SKILL_EN.md provides the full English specification for global agent hosts.
