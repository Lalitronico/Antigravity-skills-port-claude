import os
import re

# Configuration
SKILLS_DIR = r"c:\Users\HP ZBOOK\Desktop\Skills for Antigravity\Skills for Claude\skills-claude"

# Replacement rules (Regex pattern -> Replacement string)
REPLACEMENTS = [
    (r"\bthe next Claude\b", "the Assistant"),
    (r"\bClaude\b", "the Assistant"),
    (r"\bclaude\.ai\b", "the browser"),
    (r"\bClaude artifacts\b", "standalone files"),
    (r"\bRead tool\b", "view_file tool"),
    (r"\bWrite tool\b", "write_to_file tool"),
    # Add more specific tool mappings as needed
]

def migrate_skill(file_path):
    print(f"Migrating: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for pattern, replacement in REPLACEMENTS:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  -> Updated {file_path}")
        else:
            print(f"  -> No changes needed for {file_path}")
            
    except Exception as e:
        print(f"  -> ERROR: {e}")

def main():
    if not os.path.exists(SKILLS_DIR):
        print(f"Directory not found: {SKILLS_DIR}")
        return

    for root, dirs, files in os.walk(SKILLS_DIR):
        for file in files:
            if file == "SKILL.md":
                skill_path = os.path.join(root, file)
                migrate_skill(skill_path)

if __name__ == "__main__":
    main()
