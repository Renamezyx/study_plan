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


def find_studied_in_root_dir(root_dir="."):
    res = []
    for name in os.listdir(root_dir):
        full_path = os.path.join(root_dir, name)
        if os.path.isdir(full_path):
            if "day_" in name:
                res.append(int(name.split("day_")[1]))
    return res


def write_notes_to_readme(notes_list, studied_list, readme_path="README.MD"):
    with open(".readme.bak", "r", encoding="utf-8") as src, \
            open(readme_path, "w", encoding="utf-8") as dst:
        for line in src:
            matches = re.findall(r"\[ \] (\d+)", line)
            if len(matches) > 0:
                if int(matches[0]) in studied_list:
                    line = line.replace("[ ]", "[x]", 1)
            dst.write(line)
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(f"## Notes\n")
        for idx, note in enumerate(notes_list, start=1):
            f.write(f"```shell\n")
            f.write(note + "\n\n")
            f.write(f"```")


if __name__ == "__main__":
    notes = find_notes_in_main_files(".")
    studied_list = find_studied_in_root_dir()
    write_notes_to_readme(notes_list=notes, studied_list=studied_list)
    print(f"Found {len(notes)} notes and wrote them to README.MD")
