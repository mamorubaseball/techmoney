import re

file_path = "/Users/mamoru/techmoney/smci.md"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    stripped = line.strip()
    # 装飾線や【...】で囲まれた見出し行を除去
    if re.match(r'^[━─\-]+$', stripped) and len(stripped) >= 3:
        continue
    if re.match(r'^【[^】\n]+】$', stripped) and not stripped.startswith("Speaker"):
        continue
    # タイトル行（■から始まるもの）も不要なので除去
    if stripped.startswith("■"):
        continue
    new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Original script smci.md cleaned.")
