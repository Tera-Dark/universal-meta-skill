#!/usr/bin/env python3
"""
validate_skill.py
Zero-dependency static validator for Universal Meta-Skill and downstream Agent Skills.
Checks:
1. Valid frontmatter delimiters (---)
2. Required fields: name, description (non-empty)
3. Integrity of local file references (e.g., references/xxx.md)
"""

import sys
import re
from pathlib import Path

# Force UTF-8 output encoding for cross-platform stability (especially Windows CMD/PowerShell)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def parse_frontmatter(content: str):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, "Missing or malformed YAML frontmatter (must start with '---' block)"
    
    fm_raw = match.group(1)
    fields = {}
    current_key = None
    
    for line in fm_raw.splitlines():
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        key_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if key_match:
            current_key = key_match.group(1)
            val = key_match.group(2).strip()
            fields[current_key] = val
        elif current_key and line.startswith(" "):
            fields[current_key] += " " + line_clean
            
    return fields, None

def check_file_references(file_path: Path, content: str):
    broken_refs = []
    base_dir = file_path.parent
    
    # Matches patterns like references/xxx.md or `references/xxx.md`
    ref_matches = re.findall(r"[`'\"]?(references/[a-zA-Z0-9_\-/]+\.md)[`'\"]?", content)
    for ref in ref_matches:
        target = base_dir / ref
        if not target.exists():
            broken_refs.append((ref, str(target)))
            
    return broken_refs

def validate_skill_file(file_path: Path) -> bool:
    print(f"\n[CHECKING] {file_path.name}")
    
    if not file_path.exists():
        print(f"  [ERROR] File does not exist: {file_path}")
        return False
        
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Frontmatter
    fields, err = parse_frontmatter(content)
    if err:
        print(f"  [FAIL] Frontmatter error: {err}")
        return False
    print("  [OK] Frontmatter delimiters valid")
    
    # 2. Required fields
    if "name" not in fields or not fields["name"].strip():
        print("  [FAIL] Missing required field: 'name'")
        return False
    print(f"  [OK] Name verified: {fields['name']}")
    
    if "description" not in fields or not fields["description"].strip():
        print("  [FAIL] Missing required field: 'description'")
        return False
    print(f"  [OK] Description verified: {fields['description'][:60]}...")
    
    # 3. Broken references
    broken_refs = check_file_references(file_path, content)
    if broken_refs:
        for ref, abs_p in broken_refs:
            print(f"  [FAIL] Broken reference found: '{ref}' -> file not found at {abs_p}")
        return False
    print("  [OK] All referenced files exist on disk")
    
    return True

def main():
    root = Path(__file__).resolve().parent.parent
    skills_to_check = [
        root / "SKILL.md",
        root / "SKILL_EN.md"
    ]
    
    all_passed = True
    print("================================================")
    print("  Universal Meta-Skill Automated Validator")
    print("================================================")
    
    for s in skills_to_check:
        if not validate_skill_file(s):
            all_passed = False
            
    print("\n------------------------------------------------")
    if all_passed:
        print("Result: PASS (All core skills passed static validation)")
        sys.exit(0)
    else:
        print("Result: FAIL (Issues detected, see details above)")
        sys.exit(1)

if __name__ == "__main__":
    main()
