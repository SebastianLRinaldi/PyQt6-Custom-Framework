import os

BASE_DIR = os.path.join("src", "components")
IMPORTABLES = ["layout", "logic", "connections"]
INIT_FILE = os.path.join(BASE_DIR, "__init__.py")

lines = []

for widget_name in sorted(os.listdir(BASE_DIR)):
    widget_path = os.path.join(BASE_DIR, widget_name)
    if not os.path.isdir(widget_path) or widget_name.startswith("__"):
        continue

    for part in IMPORTABLES:
        file_path = os.path.join(widget_path, f"{part}.py")
        if os.path.exists(file_path):
            alias = f"{widget_name}{part}"
            line = f"from .{widget_name}.{part} import {part} as {alias}"
            lines.append(line)
    lines.append("")  # add a blank line after each widget block

with open(INIT_FILE, "w") as f:
    f.write("\n".join(lines))

print(f"Wrote imports to {INIT_FILE}")
