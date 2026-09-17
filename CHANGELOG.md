# Changelog

## 1.2.1

- **Fixed Documentation Typos**: Corrected typo `eferences/` to `references/` and fixed Markdown block formatting in `README.md`.
- **Refined Host Loading Claims**: Clarified that host discovery, loading, and runtime behaviors differ by platform and must be verified per documentation.
- **Added Real Host Capability Matrix**: Updated `host-capability-matrix.md` with actual verified records for Google Antigravity and Claude Code.
- **Added Zero-Dependency Verification Script**: Added `scripts/validate_skill.py` to statically validate frontmatter and reference integrity.
- **Added Evaluation Test Fixtures**: Added `tests/fixtures/` with test cases for ambiguous input, missing input, and security boundary violations.

## 1.2.0

- **Bilingual Architecture**: Added complete Chinese localization alongside English originals.
- Set root `SKILL.md` and `README.md` to Chinese by default for better native domestic agent and developer experience.
- Preserved `SKILL_EN.md` and `references/en/` as complete English mirrors for global cross-platform compatibility.
- Added cross-language navigation badges in documentation.

## 1.1.0

- Added a lightweight Fast Path.
- Added a minimal skill template.
- Added host capability and metadata guidance.
- Added a dedicated evaluation protocol.
- Clarified that host support and verification claims require evidence.
- Strengthened authority boundaries and migration guidance.
- Preserved a portable core with optional project extensions.

## 1.0.0

- Initial release of the universal meta-skill.
