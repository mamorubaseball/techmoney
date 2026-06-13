import re
import os

dir_path = "/Users/mamoru/techmoney/smci+20260609"
files = ["台本1.md", "台本2.md", "台本3.md"]

for file_name in files:
    file_path = os.path.join(dir_path, file_name)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        # 再度元ファイル（split_script.pyによって生成されたファイル）を読み込む必要があるので
        # 実際には、もう一度 split_script を走らせるか、もしくはこのスクリプトで現在のファイルから「【」を消すだけで大丈夫。
        # 単純に「【」で始まる行を削除する処理を行う。
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 【で始まる行や空の見出し行などを除去
        if stripped.startswith("【") or stripped.startswith("#") or stripped.startswith("---") or stripped.startswith("━") or stripped.startswith("■"):
            continue
        new_lines.append(line)
        
    # 連続する空行を整理
    content = "".join(new_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip() + "\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Re-cleaned {file_name}")
