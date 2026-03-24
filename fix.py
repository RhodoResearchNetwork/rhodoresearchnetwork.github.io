import os
import re

folder = "_rrn_taxa"

doi_target = "https://doi.org/10.1017/S0960428600001633"

def normalize(s):
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s

for filename in os.listdir(folder):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(folder, filename)

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    text = "".join(lines)
    norm = normalize(text)

    # Check if the file contains the reference at all
    if not ("kron" and "1993" in norm):
        print(f"No Kron reference found in {filename}")
        continue

    # Find the reference line
    ref_index = None
    for i, line in enumerate(lines):
        if ("Kron" in line and "(1993" in line):
            ref_index = i
            break

    if ref_index is None:
        print(f"Reference detected but reference line not found in {filename}")
        continue

    # Find DOI line (if present)
    doi_index = None
    for i, line in enumerate(lines):
        if doi_target in line:
            doi_index = i
            break

    ref_text = lines[ref_index].strip()
    replacement = f"[{ref_text}]({doi_target})\n"

    new_lines = []

    for i, line in enumerate(lines):
        if i == ref_index:
            new_lines.append(replacement)
        elif i == doi_index:
            continue  # remove DOI line if present
        else:
            new_lines.append(line)

    # If DOI was missing, append nothing — replacement already includes it

    print(f"Updated Kron  1993 reference in {filename}")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)