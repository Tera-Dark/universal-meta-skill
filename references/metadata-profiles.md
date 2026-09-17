# Metadata Profiles

## Portable core

Use only metadata required by the target standard or host. In many skill systems, the safest portable baseline is:

- `name`
- `description`

The exact accepted fields and constraints must be verified for the intended host.

## Optional extensions

Fields such as `version`, `tags`, `layer`, `upstream`, `downstream`, and `output_schema` may be useful as project metadata, but should not be assumed to affect runtime behavior unless the host documents them.

## Metadata checklist

- Is the name unique and descriptive?
- Does the description explain both capability and activation context?
- Are unsupported fields excluded from the runtime-critical frontmatter?
- Are project-only fields documented separately?
- Is the description specific enough to avoid accidental activation?
