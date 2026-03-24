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

    sci = front.get("scientificname", "").strip()
    auth = front.get("scientificnameauthorship", "")

    # Build title
    if auth:
        new_title = f"{sci} {auth}".strip()
    else:
        new_title = sci

    old_title = front.get("title", "")

    if old_title != new_title:
        print(f"Fixing {filename}: '{old_title}' → '{new_title}'")
        front["title"] = new_title
    else:
        print(f"{filename} already OK")

    # Write back
    new_front = yaml.dump(front, sort_keys=False).strip()
    new_text = f"---\n{new_front}\n---{body}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)