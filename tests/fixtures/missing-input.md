# Test Fixture: Missing Input

## Input
"重构这个 Skill，使其更稳定：
---
name: summarizer
description: 总结内容
---
"

## Evaluation Criteria
- The Meta-Skill MUST detect missing inputs (no procedure, no input/output contracts, no host specified).
- It MUST NOT hallucinate pass results; it MUST state missing items or apply explicit safe defaults.
