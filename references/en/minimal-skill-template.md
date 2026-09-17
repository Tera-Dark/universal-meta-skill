# Minimal Skill Template

Use this template for a small skill with one clear purpose.

```markdown
---
name: example-skill
description: [Specific action] when [clear trigger or user need].
---

# Example Skill

## Purpose

[One sentence describing the successful outcome.]

## When to use

Use this skill when:
- [Trigger 1]
- [Trigger 2]

Do not use it for:
- [Non-scope 1]

## Inputs

Required:
- [Input]

Optional:
- [Input]

If a required input is missing, [ask / stop / use a declared default].

## Procedure

1. [Executable step]
2. [Executable step]
3. [Check or transform result]

## Output contract

Return:
- [Exact format]
- [Required fields]

If verification is unavailable, label the result `UNKNOWN` rather than claiming success.

## Failure behavior

- [Failure case]: [response]
- [Out-of-scope case]: [response]
```
