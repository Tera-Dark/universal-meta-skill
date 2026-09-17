# Evaluation Protocol

## Evaluation levels

### Level 1 — Static review

Check:
- metadata syntax;
- trigger clarity;
- scope and non-scope;
- input/output completeness;
- contradictions;
- unsupported capability claims.

### Level 2 — Behavioral smoke test

Run:
- one normal case;
- one ambiguous case;
- one missing-input case;
- one out-of-scope case.

### Level 3 — Risk-oriented regression

Add cases for:
- authority confusion;
- malicious or irrelevant instructions in external content;
- tool failure;
- malformed input;
- behavior that previously regressed.

## Result format

```text
Status: PASS | FAIL | PARTIAL | UNKNOWN
Evidence:
- [Observed result]
Limitations:
- [Unverified condition]
Regression impact:
- [None / described impact]
```

A score may be used for internal prioritization, but it must not replace blocking quality gates.
