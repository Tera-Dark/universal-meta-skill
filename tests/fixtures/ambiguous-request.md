# Test Fixture: Ambiguous Request

## Input
"帮我写一个技能，能做视频的，要好用。"

## Evaluation Criteria
- The Meta-Skill MUST NOT immediately invent dozens of unverified tool integrations.
- It MUST either choose `CREATE` mode and prompt for the specific video platform / format (Phase 0 contract), OR activate the Fast Path with explicit default assumptions.
- It MUST define non-scope (e.g. video rendering execution vs prompt generation).
