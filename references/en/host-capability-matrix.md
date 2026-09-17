# Host Capability Matrix

This matrix records actual support across major agent platforms.
**Rule: Never claim support without evidence; use `VERIFIED` only when confirmed through reproducible tests or official documentation.**

### Status Values:

- `VERIFIED`: Confirmed via reproducible test or explicit documentation.
- `PARTIAL`: Supported with meaningful limitations or conditions.
- `UNKNOWN`: Not yet verified in an actual environment.
- `NOT_SUPPORTED`: Confirmed unavailable.

## Records

| Host | Capability | Status | Evidence / Date | Notes |
|---|---|:---:|---|---|
| **Google Antigravity** | Root `SKILL.md` discovery | **VERIFIED** | Tested (2026-09-17) | Discovered via frontmatter name and description |
| **Google Antigravity** | YAML frontmatter parsing | **VERIFIED** | Tested (2026-09-17) | Standard name/description properly indexed |
| **Google Antigravity** | Supporting file access | **VERIFIED** | Tested (2026-09-17) | Subdirectory references readable via tool calls |
| **Google Antigravity** | Script execution | **VERIFIED** | Tested (2026-09-17) | Can execute Python / Node / Shell scripts via terminal |
| **Google Antigravity** | Progressive disclosure | **VERIFIED** | Tested (2026-09-17) | Efficient on-demand reading preserves context |
| **Claude Code** | Root `SKILL.md` discovery | **VERIFIED** | Official docs / community | Follows standard skill discovery conventions |
| **Claude Code** | Reference file loading | **PARTIAL** | Community tested | Usually requires explicit prompt to inspect references |
| **Claude Code** | Script execution | **VERIFIED** | Official docs | Native bash execution supported |
| **OpenCode / OpenClaw** | Skill discovery | **UNKNOWN** | Pending test | Smoke test pending in actual CLI environment |
| **OpenAI Codex CLI** | Multi-file skill parsing | **UNKNOWN** | Pending test | Multi-file traversal pending verification |
