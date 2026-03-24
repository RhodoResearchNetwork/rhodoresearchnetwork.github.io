import os
import yaml

folder = "_rrn_taxa"

for filename in os.listdir(folder):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(folder, filename)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.startswith("---"):
        print(f"Skipping {filename}: no front matter")
        continue

    # Split front matter and body
    parts = text.split("---", 2)
    front = yaml.safe_load(parts[1])
    body = parts[2]

    changed = False

    # Ensure layout
    if "layout" not in front:
        front["layout"] = "default"
        changed = True

    # Ensure title
    if "title" not in front:
        sci = front.get("scientificname", "").strip()
        auth = front.get("scientificnameauthorship", "").strip()
        title = f"{sci} {auth}".strip()
        front["title"] = title
        changed = True

    if changed:
        print(f"Fixing {filename}")
        new_front = yaml.dump(front, sort_keys=False).strip()
        new_text = f"---\n{new_front}\n---{body}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
    else:
        print(f"{filename} already OK")