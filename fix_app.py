import os

def fix_file():
    path = r'd:\agri\backend\app.py'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove the duplicated/corrupted block in weather_alerts
    # It seems the tool inserted the new code inside the old line
    
    import re
    
    # Fix the corrupted weather_alerts block
    # Pattern 1: # â”€...â”€â”        genai.configure...
    content = re.sub(r'# [â”€]+\        genai.configure', r'# ──────────────────────────────────────────────────────────────\n        genai.configure', content)
    
    # Pattern 2: }ai.configure
    content = re.sub(r'\}ai.configure', r'}\n        genai.configure', content)

    # Remove duplicated blocks if any
    # (The tool might have added the code twice)
    
    # Let's just restore the file to a clean state by removing the mess
    # I will reach out to the known parts of the file to fix it.
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_file()
