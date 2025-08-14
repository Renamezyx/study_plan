import os
import re


def find_notes_in_main_files(root_dir="."):
    notes_list = []
    pattern = re.compile(r'notes\s*=\s*"""(.*?)"""', re.S)  # 支持多行匹配

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "main.py":
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    match = pattern.search(content)
                    if match:
                        notes_list.append(match.group(1).strip())
    return notes_list


def write_notes_to_readme(notes_list, readme_path="README.MD"):
    with open(".readme.bak", "r", encoding="utf-8") as src, \
            open(readme_path, "w", encoding="utf-8") as dst:
        for line in src:
            dst.write(line)

    with open(readme_path, "w+", encoding="utf-8") as f:
        for idx, note in enumerate(notes_list, start=1):
            f.write(f"### \n")
            f.write(f"```shell\n")
            f.write(note + "\n\n")
            f.write(f"```")


if __name__ == "__main__":
    notes = find_notes_in_main_files(".")
    write_notes_to_readme(notes)
    print(f"Found {len(notes)} notes and wrote them to README.MD")
