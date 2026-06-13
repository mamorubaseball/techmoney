import re
import os

dir_path = "/Users/mamoru/techmoney/スペースxIPO+20260608"
files = ["台本1.md", "台本2.md", "台本3.md"]

for file_name in files:
    file_path = os.path.join(dir_path, file_name)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 見出し行、区切り線、タイトルを除外
        if stripped.startswith("#") or stripped.startswith("---"):
            continue
        new_lines.append(line)
        
    # 連続する空行を整理
    content = "".join(new_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip() + "\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned {file_name}")
